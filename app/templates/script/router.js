// router.js
class Router {
    constructor() {
        this.routes = {};
    }

    addRoute(path, callback) {
        this.routes[path] = callback;
    }

    navigate() {
        const currentPath = window.location.pathname;
        const callback = this.routes[currentPath];
        if (callback) {
            callback();
        } else {
            console.error("Route not found:", currentPath);
        }
    }
}

const router = new Router();

// Add routes
router.addRoute("/", () => {
    console.log("Home page");
    // Здесь можно загрузить и отобразить контент для домашней страницы
});

router.addRoute("/about", () => {
    console.log("About page");
    // Здесь можно загрузить и отобразить контент для страницы "О нас"
});

// Инициализация роутера
window.addEventListener("popstate", () => {
    router.navigate();
});

// Инициализация роутера при загрузке страницы
window.addEventListener("load", () => {
    router.navigate();
});

// Можно также добавить навигацию с использованием ссылок
document.addEventListener("click", (event) => {
    if (event.target.tagName === "A" && event.target.href.startsWith(window.location.origin)) {
        event.preventDefault();
        const path = new URL(event.target.href).pathname;
        history.pushState(null, null, path);
        router.navigate();
    }
});
