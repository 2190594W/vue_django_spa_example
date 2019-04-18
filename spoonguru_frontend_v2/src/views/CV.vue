<template>
  <div style="text-align: center">
    <img src="../assets/profile.png" style="border-radius: 10px; width: 150px; margin-bottom: 30px;"><br/>
    <a href="cv.pdf" target="_blank">Download CV as a PDF!</a>
    <pdf
      v-for="i in numPages"
      :key="i"
      src='cv.pdf'
      :page="i"
      style="display: block;"
    ></pdf>
  </div>
</template>

<script>
import pdf from 'vue-pdf';

const loadingTask = pdf.createLoadingTask('cv.pdf');

export default {
  components: {
    pdf,
  },
  data() {
    return {
      src: loadingTask,
      numPages: undefined,
    };
  },
  mounted() {
    this.src.then((pdfInst) => {
      this.numPages = pdfInst.numPages;
    });
  },
};
</script>
