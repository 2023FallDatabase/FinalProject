<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">Add Film</router-link> |
      <router-link to="/UpdateView">Update Film</router-link>|
      <router-link to="/useComment">useComment</router-link>|
      <!--router-link to="/LoginView">Log in</router-link-->|
      <!--router-link to="/SignUp">Sign Up</router-link-->
      <a href="http://127.0.0.1:8000/login/">Log in</a>|
      <a href="http://127.0.0.1:8000/register/">Sign up</a>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
#nav a {
  font-weight: bold;
  color: #302e28;
}

#nav a.router-link-exact-active {
  color: #998f7f;
}
</style>
