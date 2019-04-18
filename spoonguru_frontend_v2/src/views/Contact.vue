<template>
  <div class="hello" style="width: 80%; text-align: center; margin: 0 auto;">
    <img src="../assets/profile.png" style="border-radius: 10px; width: 150px;">
    <h1>{{ msg }}</h1>
    <lorem add="4s"></lorem>
    <form
      id="newContactRequest"
      @submit="checkForm"
      method="post"
      v-if="formNotSubmitted"
    >

      <p v-if="errors.length" style="margin-bottom: 20px;">
        <b>Please correct the following error(s):</b>
        <ul>
          <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
        </ul>
      </p>

      <p>
        <label for="firstName">First Name: </label>
        <input
          id="firstName"
          v-model="firstName"
          type="text"
          name="firstName"
        >
      </p>

      <p>
        <label for="lastName">Last Name: </label>
        <input
          id="lastName"
          v-model="lastName"
          type="text"
          name="lastName"
        >
      </p>

      <p>
        <label for="email">Email Address: </label>
        <input
          id="email"
          v-model="email"
          type="email"
          name="email"
        >
      </p>

      <p>
        <label for="message">Message: </label>
        <textarea
          id="message"
          v-model="message"
          type="text"
          name="message"
        ></textarea>
      </p>

      <input
        type="submit"
        value="Submit"
        class="submitBtn"
      >

    </form>
    <h4 v-if="!formNotSubmitted">{{formResponseMsg}}</h4>
    <h5 v-if="!formNotSubmitted">We will get back to you as soon as possible.</h5>
  </div>
</template>

<script>
import lorem from 'vue-lorem-ipsum';

const apiUrl = "http://localhost:8000/api/";

export default {
  components: {
    lorem,
  },
  name: 'AboutMe',
  data() {
    return {
      msg: 'Contact Us',
      firstName: '',
      lastName: '',
      email: '',
      message: '',
      errors: [],
      formNotSubmitted: true,
      formResponseMsg: '',
    };
  },
  methods: {
    checkForm: function (e) {
      e.preventDefault();

      this.errors = [];

      if (!this.firstName) {
        this.errors.push("First Name required.");
      }
      if (!this.lastName) {
        this.errors.push("Last Name required.");
      }
      if (!this.email) {
        this.errors.push('Email required.');
      } else if (!this.validEmail(this.email)) {
        this.errors.push('Valid email required.');
      }
      if (!this.message) {
        this.errors.push("Message required.");
      }

      if (!this.errors.length) {
        const that = this;
        this.$http.post(apiUrl + "new_contact_request", {
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          message: this.message,
        })
        .then(function (response) {
          if (response.status === 201) {
            that.formNotSubmitted = false;
            that.formResponseMsg = response.data.message;
          }
          console.info(response);
          return true;
        })
        .catch(function (error) {
          console.error(error);
        });
      }
    },
    validEmail: function (email) {
      var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    }
  }
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
input, textarea {
    box-shadow: 0px 0px 4px #ccc;
    border: 1px gray;
    border-radius: 2px;
    width: 300px;
    flex: 3;
}
textarea {
  line-height: 70px;
}
.submitBtn {
  background-color: #41b883;
  border-radius: 3px;
  border-color: #2f865f;
  box-shadow: 1px 1px 0px #2f865f;
  width: 80px;
  height: 30px;
  margin-top: 20px;
  flex: 1;
}
form {
  margin: 40px auto;
  width: 70%;

}
form p {
  display: flex;
  flex-direction: row;
}
label {
  flex: 1;
  text-align: right;
  padding-right: 10px;
  font-weight:bold;
}
</style>
