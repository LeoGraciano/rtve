import axios from "axios";

export const api = axios.create({
    baseURL: "http://localhost:8000/api"
})

export async function getCategories() {
    const response = await api.get("/categories/")
    return response.data
}
export async function getExpenditure() {
    const response = await api.get("/expenditure/")
    return response.data
}
export async function getExpense(id: string) {
    const response = await api.get(`/expenditure/${id}`)
    return response.data
}

export async function getCategory(id: string) {
    const response = await api.get(`/categories/${id}`)
    return response.data
}