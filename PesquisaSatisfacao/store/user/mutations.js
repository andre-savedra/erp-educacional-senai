export default {
    STORE(state, payload) {
        state.user = payload;
    },
    ADMIN(state, payload) {
        state.admin = payload;
    }
}