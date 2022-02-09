<template>
  <div class="containerSystems">
    <div class="card" v-for="(sistema, index) in sistemas" :key="index">
      <h3>{{ sistema.title }}</h3>
      <hr />
      <div id="card">
        <h1 class="card-img">
          <img :src="require(`@/static/${sistema.img}`)" />
        </h1>
        <p class="card-text">
          {{ sistema.text }}
        </p>
        <router-link :to="sistema.url_to" class="btn-sistemas">OK</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      sistemas: [
        {
          title: "FIAP",
          img: "fiap.png",
          url_to: "/dashboards",
          text: "Formulario FIAP para declarar alunos com baixo desempenho",
        },
        {
          title: "Pesquisa de Satisfação",
          img: "ps.png",
          url_to: "/",
          text: "Sistema de pesquisa de satisfação dos alunos e professores sobre o senai",
        },
        {
          title: "Pesquisa de Satisfação",
          img: "ps.png",
          url_to: "/",
          text: "Sistema de pesquisa de satisfação dos alunos e professores sobre o senai",
        },
      ],
    };
  },
};
</script>

<style lang="scss">
html {
  min-height: 100%;
  background-color: #e8e6e6;
}

.containerSystems {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-content: center;
  flex-wrap: wrap;
  margin-top: 50px;
  

  .card {
    padding: 60px 0;
    margin: 0 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: auto;

    h3 {
      text-align: center;
      padding-bottom: 5px;
    }

    #card {
      height: auto;
      width: 300px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      background-color: #f4f4f4;
      box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
      align-items: center;
      margin-top: 20px;
      text-align: center;
      .card-text {
        padding: 10px;
        height: 90px;
      }

      img {
        height: 250px;
        width: 300px;
      }
    }

    .btn-sistemas {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 40px;
      width: 80%;
      margin: 15px 0;
      color: #fff;
      text-decoration: none;
      background-color: #ec1c24;

      .btn-sistemas:hover {
        color: #16c47c;
      }
    }
  }
}
</style>
