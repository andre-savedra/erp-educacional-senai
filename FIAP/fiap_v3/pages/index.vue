<template >
  <div id="form" :class="darkMode ? 'dark' : 'light'">
    <div class="sheet">
      <form class="content" @submit.prevent="submitForm">
        <div class="title-sheet">
          <h1>Ficha Individual de Avaliação Periódica</h1>
          <!-- @click="callA()" -->
        </div>

        <FieldForm
          title="Identificação"
          type="rows"
          :hiddenContent="false"
          :items="[
            ['Aluno:'], //line 1
            ['Turma:', 'Nº:', 'Data:'], //line 2
            ['Docente:', 'Disciplina:'], //line 3
            ['Analista:'], //line 4
          ]"
          :itemsDisabled="[
            ['false'], //line 1
            ['true', 'true', 'true'], //line 2  
            ['true', 'false'], //line 3
            ['false'], //line 4
          ]"
          :idUser="[idStudentSearch, false, false, idAnalistSearch]"
          @update="fiap_data_att.identification = $event"
          :innerRefs="fiap_data_att.identification"
        />

        <FieldForm
          title="Frequência"
          type="rows"
          :hiddenContent="true"
          :items="[
            ['Aulas previstas:', 'Ausências:'], //line 1
          ]"
          :itemsDisabled="[
            ['false', 'false']
          ]"
          @update="fiap_data_att.frequency = $event"
          :innerRefs="fiap_data_att.frequency"
        />

        <FieldForm
          title="Aproveitamento escolar"
          type="rows"
          :hiddenContent="true"
          :items="[
            ['Unidade avaliada:'], //line 1
            ['Nota média da turma:', 'Nota do aluno:', 'Nota de recuperação:'], //line 2
          ]"
          :itemsDisabled="[
            ['false'],
            ['false', 'false', 'false']
          ]"
          @update="fiap_data_att.schoolarEnjoyment = $event"
          :innerRefs="fiap_data_att.schoolarEnjoyment"
        />

        <FieldForm
          title="Aprendizagem"
          type="checks"
          :hiddenContent="true"
          :items="[
            'Atenção/ Concentração/ Memorização',
            'Compreensão/ Interpretação/ Análise/ Síntese',
            'Comprometimento',
            'Relacionamento interpessoal',
            'Outras situações pertinentes ao processo de aprendizagem',
          ]"
          @update="fiap_data_att.apprenticeship = $event"
          :innerRefs="fiap_data_att.apprenticeship"
        />

        <FieldForm
          title="Ocorrências"
          type="checks"
          :hiddenContent="true"
          :items="[
            'Advertência verbal',
            'Advertência escrita',
            'Afastamento temporário',
            'Cancelamento de matrícula',
          ]"
          @update="fiap_data_att.occurrence = $event"
          :innerRefs="fiap_data_att.occurrence"
        />
        <client-only placeholder="loading...">
          <Signature
            title="Ciência dos gestores do(s) processo(s):"
            :topTitle="['Gestor', 'Data', 'Assinatura']"
            :leftTitle="['Docente', 'Coordenador', 'AQV/OE']"
            @update="fiap_data_att.managerKnowledgement = $event"
            :innerRefs="fiap_data_att.managerKnowledgement"
          />

          <Signature
            title="Ciência do(s) agente(s) do processo: (Aluno/Responsável):"
            :topTitle="['Agente', 'Data', 'Assinatura']"
            :leftTitle="['Aluno', 'Responsável']"
            @update="fiap_data_att.agentKnowledgement = $event"
            :innerRefs="fiap_data_att.agentKnowledgement"
          />
        </client-only>

        <FieldForm
          title="Motivo/Observações"
          type="largerow"
          :hiddenContent="true"
          :items="[['Descrição']]"
          @update="fiap_data_att.desc = $event"
          :innerRefs="fiap_data_att.desc"
        />

        <button class="btn-save" type="submit">Salvar</button>
      </form>
    </div>

    <PopUp :type="popType" :show="showModal" v-if="showModal" />
  </div>
</template>

<style lang="scss" scoped>
@import "../static/assets/scss/mixins";
@import "../static/assets/scss/dark";

#form {
  width: 100%;
  background: var(--back-second);
  padding: 6rem 8% 2rem 8%;

  border-top: 2px solid var(--border-nav);

  .sheet {
    background: #fff;
    padding: 4rem 15%;

    .content {
      .btn-save {
        padding: 10px 35px;
        background: #cc0510;
        color: #eee;
        margin-top: 30px;
        cursor: pointer;
        width: 100%;

        &:hover {
          background: #ae050e;
        }
        &:active {
          background: #9a050d;
        }
      }

      .title-sheet {
        h1 {
          font-weight: 400;
          text-align: center;
          margin-bottom: 20px;
        }
      }
    }
  }
}

@media (max-width: 1180px) {
  #form {
    padding-right: 6%;
    padding-left: 6%;

    .sheet {
      padding: 2rem 10%;
    }
  }
}

@media (max-width: 991px) {
  #form {
    padding: 2rem 4%;

    .sheet {
      padding: 2rem 6%;
    }
  }
}
</style>

<script>
import { mapGetters } from "vuex";
import Vue from "vue";
const axios = require("axios");
export default {
  props: ["commitMethodURL"],
  data: function () {
    return {
      occ: false,
      popType: "load",
      showModal: false,
      signVal: "",
      BASE_URL: "http://localhost:8000/",
      commitMethod: "POST",
      sendVerify: 1,
      idFiapSearch: "",
      idStudentSearch: null,
      idAnalistSearch: null,
      idUserSearch: 3,
      idSubjectSearch: 1,
      mainData: {},
      isEditing: true,
      hoje: "",
      fiap_data_att: {
        identification: [
          // Row 1 index 0
          {
            aluno: null,
          },
          // Row 2 index 1
          {
            turma: null,
            ra: null,
            //2021-11-29T08:32:16-03:00
            data: null,
          },
          // Row 3 index 2
          {
            docente: null,
            disciplina: null,
          },
          // Row 4 index 3
          {
            analista: null,
          },
        ],
        frequency: [
          {
            aulasprevistas: null,
            ausencias: null,
          },
        ],
        schoolarEnjoyment: [
          {
            materia: null,
          },
          {
            notamedia: null,
            notaaluno: null,
            notarec: null,
          },
        ],
        apprenticeship: [
          {
            atencao: false,
            compreensao: false,
            comprometimento: false,
            relacionamento: false,
            outros: false,
          },
        ],
        occurrence: [
          {
            advverbal: false,
            advescrita: false,
            afastamento: false,
            cancelmatricula: false,
          },
        ],
        managerKnowledgement: [
          {
            professor: {
              sign: "Não Assinado",
              date: null,
            },
            coordenador: {
              sign: "Não Assinado",
              date: null,
            },
            QLA: {
              sign: "Não Assinado",
              date: null,
            },
          },
        ],
        agentKnowledgement: [
          {
            aluno: {
              sign: "Não Assinado",
              date: null,
            },
            responsavel: {
              sign: "Não Assinado",
              date: null,
            },
          },
        ],
        desc: [
          {
            text: null,
          },
        ],
        NON_CHANGEBLE_DATA: {
          aluno: {
            id: null,
          },
          materia: {
            id: null,
          },
          professor: {
            id: null,
          },
          turma: {
            id: null,
          },
          analista: { //added
            id: null,
          },
        },
      },
    };
  },
  // watch: {
  //   occ: function (newValue) {
  //     console.log("paramA", newValue); // won't print unless 'immediate: true'
  //   },
  // },
  computed: {
    ...mapGetters(["darkMode"]),
  },
  methods: {
    // callA: function(){
    //   console.log(this.fiap_data_att.managerKnowledgement[0].professor.sign)
    // },
    formatNumber: function (input) {
      if (input >= 0 && input <= 9) return "0" + input.toString();
      else return input.toString();
    },
    formatDate: function (input) {      
      let dt = new Date();

      if (input === null) return input;

      if (input === "frontend")
        return (
          this.formatNumber(dt.getDate()) +
          "/" +
          this.formatNumber(dt.getMonth() + 1) +
          "/" +
          dt.getFullYear() +
          " - " +
          this.formatNumber(dt.getHours()) +
          ":" +
          this.formatNumber(dt.getMinutes())
        );
      else if (input.includes("/")) {
        let val = input.split("-");
        val[0] = val[0].trim().replaceAll("/", "-"); //date
        val[1] = val[1].trim().replaceAll("/", "-"); //time
        //invert date position
        const separator = val[0].split("-");
        if (separator.length === 3)
          val[0] = separator[2] + "-" + separator[1] + "-" + separator[0];

        return val[0] + "T" + val[1] + ".000000-03:00";
      } else if (input.includes("T")) {
        let val = input.split("T");

        const separator = val[0].split("-");
        if (separator.length === 3)
          val[0] = separator[2] + "/" + separator[1] + "/" + separator[0];

        const separator2 = val[1].split(":");
        if (separator2.length >= 2)
          val[1] = separator2[0] + ":" + separator2[1];

        return val[0] + " - " + val[1];
      } else return input;
    },

    temporizer: function (initiate) {      
      const alunoIDver = document.getElementById("Aluno:");      
      
      if (alunoIDver !== null && this.fiap_data_att.NON_CHANGEBLE_DATA.aluno.id !== alunoIDver.value) 
      {
        if (initiate !== true) {
          this.fiap_data_att.NON_CHANGEBLE_DATA.aluno.id = alunoIDver.value;
          this.getStudent(this.fiap_data_att.NON_CHANGEBLE_DATA.aluno.id);
        }
      }

      const analistaIDver = document.getElementById("Analista:");
      
      if (analistaIDver !== null && this.fiap_data_att.NON_CHANGEBLE_DATA.analista.id !== analistaIDver.value) 
      {
        if (initiate !== true) {
          this.fiap_data_att.NON_CHANGEBLE_DATA.analista.id = analistaIDver.value;
          this.getAnalist(this.fiap_data_att.NON_CHANGEBLE_DATA.analista.id);          
        }
      }

      // console.log("this.fiap_data_att.NON_CHANGEBLE_DATA.analista.id", this.fiap_data_att.NON_CHANGEBLE_DATA.analista.id);
      // console.log("this.fiap_data_att.identification[3].analista", this.fiap_data_att.identification[3].analista);
      // console.log("this.idAnalistSearch",this.idAnalistSearch);
      // console.log(" ");


      setTimeout(this.temporizer, 1000);
    },
    getFiap: async function (fiapID) {
      const FiapResponse = await axios.get(
        this.BASE_URL + "fiap/" + fiapID + "/"
      );

      // Student Data an ID setter
      this.getStudent(FiapResponse.data.aluno);
      this.fiap_data_att.NON_CHANGEBLE_DATA.aluno.id = FiapResponse.data.aluno;
      this.idStudentSearch = FiapResponse.data.aluno;
      
      // Class Data and ID setter
      this.getClass(FiapResponse.data.turma);
      this.fiap_data_att.NON_CHANGEBLE_DATA.turma.id = FiapResponse.data.turma;

      // User Data and ID setter
      this.getUser(FiapResponse.data.usuario);
      this.fiap_data_att.NON_CHANGEBLE_DATA.professor.id =
        FiapResponse.data.usuario;

      // Subject Data da ID setter
      this.getSubject(FiapResponse.data.materia);
      this.fiap_data_att.NON_CHANGEBLE_DATA.materia.id =
        FiapResponse.data.materia;
      
      // Analist Data da ID setter
      this.getAnalist(FiapResponse.data.analista);
      this.fiap_data_att.NON_CHANGEBLE_DATA.analista.id =
        FiapResponse.data.analista;

      // Fiap Remainings usage based on ID FIAP
      this.getFrequency(fiapID);
      this.getEnjoyment(fiapID);
      this.getApprennticeship(fiapID);
      this.getOccurrence(fiapID);
      this.getSigns(fiapID);
      this.getObservations(fiapID);
      // Initial Day for FIAP
      this.fiap_data_att.identification[1].data = this.formatDate(
        FiapResponse.data.dataInicio
      );
      //this.getFrequency(fiapID)
      //this.getApprennticeship(fiapID)
    },

    // Individual Getters Function
    getStudent: async function (studentID) {
      this.fiap_data_att.NON_CHANGEBLE_DATA.aluno.id = studentID;
      const studentResponse = await axios.get(
        this.BASE_URL + "aluno/" + studentID
      );
      this.fiap_data_att.identification[0].aluno = studentResponse.data.nome;
      this.fiap_data_att.identification[1].ra = studentResponse.data.ra;
      this.getClass(studentResponse.data.turma);
    },
    getClass: async function (classID) {
      if (classID !== undefined) {
        this.fiap_data_att.NON_CHANGEBLE_DATA.turma.id = classID;
        const classResponse = await axios.get(
          this.BASE_URL + "turma/" + classID
        );
        this.fiap_data_att.identification[1].turma = await classResponse.data
          .nome;
      }
    },
    getUser: async function (userID) {      
      const userResponse = await axios.get(this.BASE_URL + "usuario/" + userID);
      this.fiap_data_att.NON_CHANGEBLE_DATA.professor.id = userResponse.data[0].id;
      this.fiap_data_att.identification[2].docente = userResponse.data[0].nome;
    },
    getAnalist: async function (analistID) {
      const userResponse = await axios.get(this.BASE_URL + "analista/" + analistID);
      this.fiap_data_att.NON_CHANGEBLE_DATA.analista.id = userResponse.data[0].id;
      this.fiap_data_att.identification[3].analista = userResponse.data[0];
    },
    getSubject: async function (subjectID) {
      this.fiap_data_att.NON_CHANGEBLE_DATA.materia.id = subjectID;
      const subjectResponse = await axios.get(
        this.BASE_URL + "materia/" + subjectID
      );
      this.fiap_data_att.identification[2].disciplina =
        subjectResponse.data.nome;
      this.fiap_data_att.schoolarEnjoyment[0].materia =
        subjectResponse.data.nome;
    },

    // Directly Fiao Related Functions
    getFrequency: async function (fiapID) {
      const frequencyResponse = await axios.get(
        this.BASE_URL + "frequencia/" + fiapID
      );
      this.fiap_data_att.frequency[0].aulasprevistas =
        frequencyResponse.data.aulasprevistas;
      this.fiap_data_att.frequency[0].ausencias =
        frequencyResponse.data.ausencias;
    },

    getEnjoyment: async function (fiapID) {
      const schoolarEnjoymentResponse = await axios.get(
        this.BASE_URL + "aproveitamento/" + fiapID
      );
      this.fiap_data_att.schoolarEnjoyment[1].notamedia =
        schoolarEnjoymentResponse.data.notamedia;
      this.fiap_data_att.schoolarEnjoyment[1].notaaluno =
        schoolarEnjoymentResponse.data.notaaluno;
      this.fiap_data_att.schoolarEnjoyment[1].notarec =
        schoolarEnjoymentResponse.data.notarec;
    },

    getApprennticeship: async function (fiapID) {
      const apprennticeshipResponse = await axios.get(
        this.BASE_URL + "aprendizagem/" + fiapID
      );

      this.fiap_data_att.apprenticeship[0].atencao =
        apprennticeshipResponse.data.atencao;
      this.fiap_data_att.apprenticeship[0].compreensao =
        apprennticeshipResponse.data.compreensao;
      this.fiap_data_att.apprenticeship[0].comprometimento =
        apprennticeshipResponse.data.comprometimento;
      this.fiap_data_att.apprenticeship[0].relacionamento =
        apprennticeshipResponse.data.relacionamento;
      this.fiap_data_att.apprenticeship[0].outros =
        apprennticeshipResponse.data.outros;
    },
    getOccurrence: async function (fiapID) {
      const occurrenceResponse = await axios.get(
        this.BASE_URL + "ocorrencia/" + fiapID
      );
      this.fiap_data_att.occurrence[0].advverbal =
        occurrenceResponse.data.advverbal;
      this.fiap_data_att.occurrence[0].advescrita =
        occurrenceResponse.data.advescrita;
      this.fiap_data_att.occurrence[0].afastamento =
        occurrenceResponse.data.afastamento;
      this.fiap_data_att.occurrence[0].cancelmatricula =
        occurrenceResponse.data.cancelmatricula;
    },
    getSigns: async function (fiapID) {
      const signsResponse = await axios.get(
        this.BASE_URL + "assinatura/" + fiapID
      );
      this.fiap_data_att.managerKnowledgement[0].professor.sign =
        signsResponse.data.docente;
      this.fiap_data_att.managerKnowledgement[0].coordenador.sign =
        signsResponse.data.coordenador;
      this.fiap_data_att.managerKnowledgement[0].QLA.sign =
        signsResponse.data.social;
      this.fiap_data_att.agentKnowledgement[0].aluno.sign =
        signsResponse.data.aluno;
      this.fiap_data_att.agentKnowledgement[0].responsavel.sign =
        signsResponse.data.responsavel;

      this.fiap_data_att.managerKnowledgement[0].professor.date =
        this.formatDate(signsResponse.data.docenteData);
      this.fiap_data_att.managerKnowledgement[0].coordenador.date =
        this.formatDate(signsResponse.data.coordenadorData);
      this.fiap_data_att.managerKnowledgement[0].QLA.date = 
        this.formatDate(signsResponse.data.socialData);
      this.fiap_data_att.agentKnowledgement[0].aluno.date = 
        this.formatDate(signsResponse.data.alunoData);
      this.fiap_data_att.agentKnowledgement[0].responsavel.date =
        this.formatDate(signsResponse.data.responsavelData);
    },
    getObservations: async function (fiapID) {
      const obsResponse = await axios.get(
        this.BASE_URL + "observacao/" + fiapID
      );
      this.fiap_data_att.desc[0].text = obsResponse.data.observacao;
    },

    // Initial Form Sender call
    async submitForm() {
      this.popType = "load";
      this.showModal = true;

      await this.saveMateria();
      await this.saveFiap();
      this.saveFrequency();
      this.saveSchoolarEnjoyment();
      this.saveApprenticeship();
      this.saveSign();
      this.saveOccurrence();
      this.saveObservation();

      setTimeout(() => {
        if (this.sendVerify) {
          this.popType = "success";

          // setTimeout(() => {this.$router.push('monitoring');  },1000);
        } else {
          this.popType = "error";
        }
      }, 2000);
    },

    // Saving Functions

    saveMateria: async function () {
      console.log("Salvando matéria....");
      if (
        this.fiap_data_att.identification[2].disciplina !== null &&
        this.fiap_data_att.identification[2].disciplina !== undefined
      ) {
        this.mainData = {
          nome: this.fiap_data_att.identification[2].disciplina,
        };

        await axios({
          method: 'POST',
          url: this.BASE_URL + "materia/",
          data: [this.mainData],
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => {
            this.sendVerify !== 0
              ? (this.sendVerify = 1)
              : (this.sendVerify = 0);

            console.log("RESPOSTA", response);
            const materiaId = response.data.materia[0].id;
            if (materiaId !== undefined && materiaId !== null) {
              this.fiap_data_att.NON_CHANGEBLE_DATA.materia.id = materiaId;
            } else {
              this.fiap_data_att.NON_CHANGEBLE_DATA.materia.id = "error";
            }
            //console.log('token', response);
            console.log("Materia salva");
          })
          .catch((response) => {
            this.sendVerify = 0;
            //console.log('error', response)
            console.log("Materia BO");
          });
      }
    },

    saveFiap: async function () {
      this.mainData = {
        progresso: "1",
        aluno: this.fiap_data_att.NON_CHANGEBLE_DATA.aluno.id,
        turma: this.fiap_data_att.NON_CHANGEBLE_DATA.turma.id,
        materia: this.fiap_data_att.NON_CHANGEBLE_DATA.materia.id,
        dataInicio: this.formatDate(this.fiap_data_att.identification[1].data),
        // dataFinal: this.formatDate(this.fiap_data_att.identification[1].data),
        usuario: this.fiap_data_att.NON_CHANGEBLE_DATA.professor.id,
        analista: this.fiap_data_att.NON_CHANGEBLE_DATA.analista.id,
      };

      console.log("main data:");
      console.log(this.mainData);

      await axios({
        method: this.commitMethod,
        url:
          this.BASE_URL +
          "fiap/" +
          (this.commitMethod === "POST" ? "" : this.idFiapSearch + "/"),
        data: this.commitMethod === "POST" ? [this.mainData] : this.mainData,
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          this.sendVerify !== 0 ? (this.sendVerify = 1) : (this.sendVerify = 0);
          //console.log('token', response);
        })
        .catch((response) => {
          this.sendVerify = 0;
          //console.error('error', response);
        });
    },
    saveFrequency: async function () {
      (this.mainData = {
        aulasprevistas:
          this.fiap_data_att.frequency[0].aulasprevistas !== null
            ? this.fiap_data_att.frequency[0].aulasprevistas
            : 0,
        ausencias:
          this.fiap_data_att.frequency[0].ausencias !== null
            ? this.fiap_data_att.frequency[0].ausencias
            : 0,
      }),
        await axios({
          method: this.commitMethod,
          url:
            this.BASE_URL +
            "frequencia/" +
            (this.commitMethod === "POST" ? "" : this.idFiapSearch + "/"),
          data: this.commitMethod === "POST" ? [this.mainData] : this.mainData,
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => {
            this.sendVerify !== 0
              ? (this.sendVerify = 1)
              : (this.sendVerify = 0);
            //console.log('token', response);
          })
          .catch((response) => {
            this.sendVerify = 0;
            //console.log('error', response)
          });
    },
    saveSchoolarEnjoyment: async function () {
      (this.mainData = {
        materia:
          this.fiap_data_att.NON_CHANGEBLE_DATA.materia.id !== null
            ? this.fiap_data_att.NON_CHANGEBLE_DATA.materia.id
            : 0,
        notamedia:
          this.fiap_data_att.schoolarEnjoyment[1].notamedia !== null
            ? this.fiap_data_att.schoolarEnjoyment[1].notamedia
            : 0,
        notaaluno:
          this.fiap_data_att.schoolarEnjoyment[1].notaaluno !== null
            ? this.fiap_data_att.schoolarEnjoyment[1].notaaluno
            : 0,
        notarec:
          this.fiap_data_att.schoolarEnjoyment[1].notarec !== null
            ? this.fiap_data_att.schoolarEnjoyment[1].notarec
            : 0,
      }),
        await axios({
          method: this.commitMethod,
          url:
            this.BASE_URL +
            "aproveitamento/" +
            (this.commitMethod === "POST" ? "" : this.idFiapSearch + "/"),
          data: this.commitMethod === "POST" ? [this.mainData] : this.mainData,
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => {
            this.sendVerify !== 0
              ? (this.sendVerify = 1)
              : (this.sendVerify = 0);
            //console.log('token', response);
          })
          .catch((response) => {
            this.sendVerify = 0;
            //console.error('error', response);
          });
    },
    saveApprenticeship: async function () {
      (this.mainData = {
        atencao:
          this.fiap_data_att.apprenticeship[0].atencao !== null
            ? this.fiap_data_att.apprenticeship[0].atencao
            : 0,
        compreensao:
          this.fiap_data_att.apprenticeship[0].compreensao !== null
            ? this.fiap_data_att.apprenticeship[0].compreensao
            : 0,
        comprometimento:
          this.fiap_data_att.apprenticeship[0].comprometimento !== null
            ? this.fiap_data_att.apprenticeship[0].comprometimento
            : 0,
        relacionamento:
          this.fiap_data_att.apprenticeship[0].relacionamento !== null
            ? this.fiap_data_att.apprenticeship[0].relacionamento
            : 0,
        outros:
          this.fiap_data_att.apprenticeship[0].outros !== null
            ? this.fiap_data_att.apprenticeship[0].outros
            : 0,
      }),
        await axios({
          method: this.commitMethod,
          url:
            this.BASE_URL +
            "aprendizagem/" +
            (this.commitMethod === "POST" ? "" : this.idFiapSearch + "/"),
          data: this.commitMethod === "POST" ? [this.mainData] : this.mainData,
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => {
            this.sendVerify !== 0
              ? (this.sendVerify = 1)
              : (this.sendVerify = 0);
            //console.log('token', response);
          })
          .catch((response) => {
            this.sendVerify = 0;
            //console.error('error', response);
          });
    },
    saveOccurrence: async function () {
      (this.mainData = {
        advverbal:
          this.fiap_data_att.occurrence[0].advverbal !== null
            ? this.fiap_data_att.occurrence[0].advverbal
            : 0,
        advescrita:
          this.fiap_data_att.occurrence[0].advescrita !== null
            ? this.fiap_data_att.occurrence[0].advescrita
            : 0,
        afastamento:
          this.fiap_data_att.occurrence[0].afastamento !== null
            ? this.fiap_data_att.occurrence[0].afastamento
            : 0,
        cancelmatricula:
          this.fiap_data_att.occurrence[0].cancelmatricula !== null
            ? this.fiap_data_att.occurrence[0].cancelmatricula
            : 0,
      }),
        await axios({
          method: this.commitMethod,
          url:
            this.BASE_URL +
            "ocorrencia/" +
            (this.commitMethod === "POST" ? "" : this.idFiapSearch + "/"),
          data: this.commitMethod === "POST" ? [this.mainData] : this.mainData,
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => {
            this.sendVerify !== 0
              ? (this.sendVerify = 1)
              : (this.sendVerify = 0);
            //console.log('token', response);
          })
          .catch(function (error) {
            this.sendVerify = 0;
            // if (error.response) {
            //   if(error.response.status === 500){
            //     async () => {
            //       await axios({
            //       method: 'POST',
            //       url: this.BASE_URL+ 'ocorrencia/',
            //       data: [this.mainData],
            //       headers: {
            //           'Content-Type': 'application/json',
            //       }
            //       }).then((response) => {
            //         this.sendVerify !== 0 ? this.sendVerify = 1 : this.sendVerify = 0;
            //         //console.log('token', response);
            //       }).catch((response) => {
            //         this.sendVerify = 0
            //         console.error('error', response);
            //       });
            //     }
            //   }
            // }
          });
    },
    saveSign: async function () {
      (this.mainData = {
        docente: this.fiap_data_att.managerKnowledgement[0].professor.sign,
        docenteData: this.formatDate(this.fiap_data_att.managerKnowledgement[0].professor.date),
        coordenador: this.fiap_data_att.managerKnowledgement[0].coordenador.sign,
        coordenadorData: this.formatDate(this.fiap_data_att.managerKnowledgement[0].coordenador.date),
        social: this.fiap_data_att.managerKnowledgement[0].QLA.sign,
        socialData: this.formatDate(this.fiap_data_att.managerKnowledgement[0].QLA.date),
        aluno: this.fiap_data_att.agentKnowledgement[0].aluno.sign,
        alunoData: this.formatDate(this.fiap_data_att.agentKnowledgement[0].aluno.date),
        responsavel: this.fiap_data_att.agentKnowledgement[0].responsavel.sign,
        responsavelData: this.formatDate(this.fiap_data_att.agentKnowledgement[0].responsavel.date),
      }),
        await axios({
          method: this.commitMethod,
          url:
            this.BASE_URL +
            "assinatura/" +
            (this.commitMethod === "POST" ? "" : this.idFiapSearch + "/"),
          data: this.commitMethod === "POST" ? [this.mainData] : this.mainData,
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => {
            this.sendVerify !== 0
              ? (this.sendVerify = 1)
              : (this.sendVerify = 0);
            //console.log('token', response);
          })
          .catch((response) => {
            this.sendVerify = 0;
            //console.error('error', response);
          });
    },

    saveObservation: async function () {
      console.log(this.fiap_data_att.desc[0].text);
      this.mainData = {
        observacao:
          this.fiap_data_att.desc[0].text !== null
            ? this.fiap_data_att.desc[0].text
            : "Sem Observações",
        data: new Date(),
      };
      if (this.commitMethod === "PUT") {
        this.mainData["fiap"] = this.idFiapSearch;
      }

      await axios({
        method: this.commitMethod,
        url:
          this.BASE_URL +
          "observacao/" +
          (this.commitMethod === "POST" ? "" : this.idFiapSearch + "/"),
        data: this.commitMethod === "POST" ? [this.mainData] : this.mainData,
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          this.sendVerify !== 0 ? (this.sendVerify = 1) : (this.sendVerify = 0);
          //console.log('token', response);
        })
        .catch((response) => {
          this.sendVerify = 0;
          //console.error('error', response);
        });
    },

    // PUT commit Functions ^

    // prevent reload
    preventNav(event) {
      if (!this.isEditing) return;
      event.preventDefault();
      event.returnValue = "";
    },
    // prevent destroy
    beforeDestroy() {
      window.removeEventListener("beforeunload", this.preventNav);
    },
    // prevent navigation
    beforeRouteLeave(to, from, next) {
      const answer = window.confirm(
        "Do you really want to leave? you have unsaved changes!"
      );
      if (answer) {
        next();
      } else {
        next(false);
      }
    },
  },
  created() {
    
    if (this.$route.params.token != undefined) {
      this.idStudentSearch = this.$route.params.idAluno;
      this.commitMethod = this.$route.params.mthd;
      this.idFiapSearch = this.$route.params.fiapID;
      this.idAnalistSearch = this.$route.params.idAnalista;
      this.getFiap(this.$route.params.fiapID);
      console.log("IFFFFFFFFFFFFFFFFFFF");
    } else {
      //this.getStudent(this.idStudentSearch);
      this.getUser(this.idUserSearch);
      this.getSubject(this.idSubjectSearch);
      // this.fiap_data_att.identification[1].data = this.hoje;
      this.fiap_data_att.identification[1].data = this.formatDate("frontend");
      console.log("ELSEEEEEEEEEEE");
    }

    // if(this.commitMethod === 'POST'){
    //   this.fiap_data_att.identification[1].data = this.hoje;
    //   this.getStudent(this.idStudentSearch);
    //   this.getUser(this.idUserSearch);
    //   this.getSubject(this.idSubjectSearch);

    // }else if(this.commitMethod === 'PUT'){

    //   if(this.idFiapSearch != null){
    //     this.getFiap(this.idFiapSearch);
    //   }
    // }else{

    // }
    
  },
  mounted() {
    this.temporizer(true);
  },
  beforeMount() {
    window.addEventListener("beforeunload", this.preventNav);
    this.$once("hook:beforeDestroy", () => {
      window.removeEventListener("beforeunload", this.preventNav);
    });
  },
};
</script>
