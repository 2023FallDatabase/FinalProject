<template>
  <div>
    <header>
      <h1>Update Film</h1>
    </header>
    <form @submit.prevent="UpdateFilm">
      <table>
        <tbody>
          <tr>
            <td><label for="name">ID:</label></td>
            <td>
              <input type="text" id="ID" v-model="film.showId" required />
            </td>
          </tr>
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
      <button type="submit">Update Film</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      film: {
        name: "",
        country: "",
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
    UpdateFilm() {
      // Convert cast and catalog input strings to arrays
      this.film.cast = this.castInput.split(",").map((item) => item.trim());
      this.film.catalog = this.catalogInput
        .split(",")
        .map((item) => item.trim());

      // Emit an event to notify the parent component with the new film data
      this.$emit("Update-film", this.film);

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
