<template>
  <div class="signup-container">
    <h1>Sign Up</h1>
    <form @submit.prevent="signUp">
      <label for="username">Username:</label>
      <input
        type="text"
        id="username"
        v-model="username"
        required
        pattern="[a-zA-Z0-9@/./+/-/_]{1,150}"
        title="Letters, digits and @/./+/-/_ only. Maximum length: 150"
      />

      <label for="firstName">First Name:</label>
      <input type="text" id="firstName" v-model="firstName" required />

      <label for="email">Email Address:</label>
      <input type="email" id="email" v-model="email" required />

      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required />

      <label for="confirmPassword">Password Confirmation:</label>
      <input
        type="password"
        id="confirmPassword"
        v-model="confirmPassword"
        required
      />

      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      firstName: "",
      email: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    signUp() {
      // Add your sign-up logic here
      // For a simple example, we'll just log the entered data
      console.log("Username:", this.username);
      console.log("First Name:", this.firstName);
      console.log("Email:", this.email);
      console.log("Password:", this.password);

      // You may want to send the data to your backend for further processing
    },
  },
};
</script>

<style scoped>
.signup-container {
  max-width: 300px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin-top: 50px;
}

h1 {
  text-align: center;
  color: #a1d573;
}

label {
  display: block;
  margin-bottom: 8px;
}

input {
  width: 100%;
  padding: 8px;
  margin-bottom: 16px;
  box-sizing: border-box;
}

button {
  background-color: #a1d573;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
</style>
