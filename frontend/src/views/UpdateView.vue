<template>
  <div>
    <header>
      <h1>Update Film</h1>
    </header>
    <form @submit.prevent="UpdateFilm">
      <table>
        <tbody>
          <tr>
            <td><label for="show_id">ID:</label></td>
            <td>
              <input type="text" id="show_id" v-model="film.show_id" required />
            </td>
          </tr>
          <tr>
            <td><label for="title">Name:</label></td>
            <td>
              <input type="text" id="title" v-model="film.title" />
            </td>
          </tr>
          <tr>
            <td><label for="country">Country:</label></td>
            <td>
              <input type="text" id="country" v-model="film.country"  />
            </td>
          </tr>
          <tr>
            <td><label for="type">Type:</label></td>
            <td>
              <input type="text" id="type" v-model="film.type"  />
            </td>
          </tr>
          <tr>
            <td><label for="director">Director:</label></td>
            <td>
              <input type="text" id="director" v-model="film.director"  />
            </td>
          </tr>
          <tr>
            <td><label for="rating">Rating:</label></td>
            <td>
              <input type="text" id="rating" v-model="film.rating"  />
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
                
              />
            </td>
          </tr>
          <tr>
            <td><label for="catalog">Catalog (comma-separated):</label></td>
            <td><input type="text" id="catalog" v-model="catalogInput" /></td>
          </tr>
        </tbody>
      </table>
      <button type="submit">Update Film</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      film: {
        show_id: "",
        title: "",
        country: "",
        type: "",
        director: "",
        rating: "",
        cast: [],
        duration: "",
        release_year: 0,
        catalog: [],
      },
      castInput: "",
      catalogInput: "",
    };
  },
  methods: {
    UpdateFilm() {
      // Convert cast and catalog input strings to arrays
      this.film.cast = this.castInput.split(",").map((item) => item.trim());
      this.film.catalog = this.catalogInput
        .split(",")
        .map((item) => item.trim());

      // Emit an event to notify the parent component with the new film data
      this.$emit("Update-film", this.film);
      console.log(this.film.show_id);
      axios
        .patch(`/api/OneForm/${this.film.show_id}`, {
          country: this.film.country,
          type: this.film.type,
          title: this.film.title,
          cast: this.film.cast[0],
          duration: this.film.duration,
          catalog: this.film.catalog[0],
          release_year: this.film.release_year,
          director: this.film.director,
          rating: this.film.rating
        })
        .then(response =>{
            console.log(response)
        })
        .catch(error =>{
            console.log(error)
        })
      // Clear form fields
      this.film = {
        title: "",
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
/* Your styling for the UpdateFilm component */
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
