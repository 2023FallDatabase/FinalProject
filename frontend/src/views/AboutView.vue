<template>
  <div>
    <header>
      <h1>Add Film</h1>
    </header>
    <form @submit.prevent="addFilm">
      <table>
        <tbody>
          <tr>
            <td><label for="name">Name:</label></td>
            <td>
              <input type="text" id="name" v-model="film.name" required />
            </td>
          </tr>
          <tr>
            <td><label for="country">Country:</label></td>
            <td>
              <input type="text" id="country" v-model="film.country" required />
            </td>
          </tr>
          <tr>
            <td><label for="name">Type:</label></td>
            <td>
              <input type="text" id="type" v-model="film.type" required />
            </td>
          </tr>
          <tr>
            <td><label for="director">Director:</label></td>
            <td>
              <input type="text" id="director" v-model="film.director" required />
            </td>
          </tr>
          <tr>
            <td><label for="rating">Rating:</label></td>
            <td>
              <input type="text" id="rating" v-model="film.rating" required />
            </td>
          </tr>
          <tr>
            <td><label for="cast">Cast (comma-separated):</label></td>
            <td><input type="text" id="cast" v-model="castInput" /></td>
          </tr>
          <tr>
            <td><label for="duration">Duration:</label></td>
            <td>
              <input
                type="text"
                id="duration"
                v-model="film.duration"
                required
              />
            </td>
          </tr>
          <tr>
            <td><label for="releaseYear">Release Year:</label></td>
            <td>
              <input
                type="text"
                id="releaseYear"
                v-model="film.release_year"
                required
              />
            </td>
          </tr>
          <tr>
            <td><label for="catalog">Catalog (comma-separated):</label></td>
            <td><input type="text" id="catalog" v-model="catalogInput" /></td>
          </tr>
        </tbody>
      </table>
      <button type="submit">Add Film</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      film: {
        name: "",
        country: "",
        type: "",
        director: "",
        rating: "",
        cast: [],
        duration: "",
        release_year: "",
        catalog: [],
      },
      castInput: "",
      catalogInput: "",
    };
  },
  methods: {
    async addFilm() {
      // Convert cast and catalog input strings to arrays
      this.film.cast = this.castInput.split(",").map((item) => item.trim());
      this.film.catalog = this.catalogInput
        .split(",")
        .map((item) => item.trim());
      // Emit an event to notify the parent component with the new film data
      this.$emit("add-film", this.film);

      let sid='';
      let len=Math.floor(Math.random()*(5))+6;
      const numbers='0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM';  
      for (let i=0;i<len;i++){
          sid=sid+numbers.charAt(Math.random()*numbers.length);
      }
      for (let k=0;k<this.film.cast.length;k++){
        for (let i=0;i<this.film.catalog.length;i++){
          let formData = {
            show_id: sid,
            title: this.film.name,
            type: this.film.type,
            director: this.film.director,
            cast: this.film.cast[k],
            rating: this.film.rating,
            duration: this.film.duration,
            catalog: this.film.catalog[i],
            country: this.film.country,
            release_year: this.film.release_year,
            average_score: 0,
            score_count: 0
          }
          await axios
          .post("/api/AllForm/", formData)
          .then(response =>{
              console.log(response)
          })
          .catch(error =>{
              console.log(error)
          })
        }
        
      }

      for (let i=0;i<this.film.cast.length;i++){
        let formData = {
          show_id: sid,
          cast: this.film.cast[i],
        }
        await axios
        .post("/api/AllCast/", formData)
        .then(response =>{
            console.log(response)
        })
        .catch(error =>{
            console.log(error)
        })
      }
      
      console.log(sid);
      console.log(this.film);
      console.log(this.film.name);
      

      // Clear form fields
      this.film = {
        name: "",
        country: "",
        rating: "",
        cast: [],
        duration: "",
        release_year: "",
        catalog: [],
      };
      this.castInput = "";
      this.catalogInput = "";
    },
  },
};
</script>

<style scoped>
/* Your styling for the AddFilm component */
table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

header {
  background-color: #a1d573;
  color: #fff;
  padding: 10px 0;
  text-align: center;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

td {
  padding: 10px;
  border: 1px solid #ddd;
}

label {
  font-weight: bold;
}
</style>
