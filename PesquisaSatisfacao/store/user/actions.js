// import axios from "axios";

export default {
    getUser(context) {
        return this.$axios.$get("http://localhost:3004/users")
            .then((response) => {
                context.commit('STORE', response);
                console.log("response", response);
                return response;
            });
    },
    setAdmin(context, payload) {
        console.log("payload");
        console.log(payload);
        context.commit('ADMIN', payload);
    },
    getDjangoUser(context) {
        return this.$axios.$get("http://localhost:8001/api/v1/Turma")
            .then((response) => {
                console.log("USUÁRIO DJANGO");
                console.log(response);
            });
    }
}