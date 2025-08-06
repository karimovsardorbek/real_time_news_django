const shownArticleIds = new Set();

async function fetchArticles() {
  try {
    const res = await fetch('http://localhost:8010/api/articles/');
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    const articles = await res.json();
    articles.reverse().forEach(addArticleToDOM);
  } catch (err) {
    console.error("Failed to fetch articles:", err);
  }
}

function addArticleToDOM(article) {
  if (shownArticleIds.has(article.id)) return;

  const card = renderArticle(article);
  document.getElementById('news-list').prepend(card);
  shownArticleIds.add(article.id);
}

function renderArticle(article) {
  const card = document.createElement('div');
  card.className = 'news-card';
  console.log(`Rendering article ${article.id} with image: ${article.image}`); // Debug log

  if (article.image) {
    const img = document.createElement('img');
    img.src = article.image;
    img.alt = article.title || 'Article image';
    img.className = 'news-image';
    img.onload = () => console.log(`Image loaded for article ${article.id}`);
    img.onerror = () => {
      console.warn(`Failed to load image for article ${article.id}: ${article.image}`);
      img.style.display = 'none'; // Hide broken images
    };
    card.appendChild(img);
  }

  const title = document.createElement('div');
  title.className = 'news-title';
  title.textContent = article.title || 'Untitled';
  card.appendChild(title);

  const meta = document.createElement('div');
  meta.className = 'news-meta';
  meta.textContent = `${article.author ? article.author + ' • ' : ''}${new Date(article.publication_date).toLocaleString()}`;
  card.appendChild(meta);

  const content = document.createElement('div');
  content.className = 'news-content';
  content.textContent = article.summary || 'No summary available';
  card.appendChild(content);

  return card;
}

const socket = new WebSocket('ws://localhost:8010/ws/news/');

socket.onopen = () => {
  console.log("✅ WebSocket connected");
};

socket.onmessage = (e) => {
  try {
    const article = JSON.parse(e.data);
    console.log("WebSocket message received:", article); // Debug log
    addArticleToDOM(article);
  } catch (err) {
    console.error("Failed to parse WebSocket message:", err);
  }
};

socket.onclose = () => {
  console.warn("⚠️ WebSocket closed. Attempting to reconnect in 3s...");
  setTimeout(() => {
    const newSocket = new WebSocket('ws://localhost:8010/ws/news/');
    newSocket.onopen = socket.onopen;
    newSocket.onmessage = socket.onmessage;
    newSocket.onclose = socket.onclose;
    newSocket.onerror = socket.onerror;
  }, 3000);
};

socket.onerror = (err) => {
  console.error("❌ WebSocket error:", err);
};

fetchArticles();