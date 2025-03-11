import axios from "axios";

const api = axios.create({
    baseURL: process.env.REACT_PUBLIC_API_BASE_URL || "http://localhost:8000",
});

export default api;