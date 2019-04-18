<template>
  <div class="hello" style="width: 80%; text-align: center; margin: 0 auto;">
    <img src="../assets/profile.png" style="border-radius: 10px; width: 150px;">
    <h1>{{ msg }}</h1>
    <lorem add="2p"></lorem>
    <h2 style="margin-top: 5%">Essential Links</h2>
    <ul>
      <li>
        <a
          href="https://cwatson.dev"
          target="_blank"
        >
          Website
        </a>
      </li>
      <li>
        <a
          href="https://www.linkedin.com/in/chrismdwatson"
          target="_blank"
        >
          LinkedIn
        </a>
      </li>
      <li>
        <a
          href="https://github.com/2190594W"
          target="_blank"
        >
          GitHub
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import lorem from 'vue-lorem-ipsum';

export default {
  components: {
    lorem,
  },
  name: 'AboutMe',
  data() {
    return {
      msg: 'About Me',
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
  margin-top: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
