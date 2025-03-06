import axios from "axios";

// Criando a instância do axios com a URL base do backend
const api = axios.create({
    baseURL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8080", // detecta ambiente docker ou localhost.
});

export default api;
