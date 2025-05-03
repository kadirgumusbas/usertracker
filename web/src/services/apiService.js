import axios from "axios";

const apiUrl = "http://127.0.0.1:8000"
const query = {
    users: "users",
    todos: "todos?user",
    posts: "posts?user",
    comments: "comments?post",
    albums: "albums?user",
    photos: "photos?album",
}

export const getRequest = (request, Id = -1) => {
    if (Id === -1) {
        return axios.get(`${apiUrl}/${query[request]}/`)
    }
    return axios.get(`${apiUrl}/${query[request]}=${Id}`)
}