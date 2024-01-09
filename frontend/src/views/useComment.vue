<template>
  <table>
    <thead>
      <tr>
        <th class="table-header-cell">
          <input v-model="searchID" @input="search" placeholder="SEARCH ID" />
        </th>
        <th class="table-header-cell">
          <input
            v-model="searchName"
            @input="search"
            placeholder="SEARCH NAME"
          />
        </th>
        <th class="table-header-cell">
          <input
            v-model="searchCOUNTRY"
            @input="search"
            placeholder="SEARCH COUNTRY"
          />
        </th>
        <th class="table-header-cell">
          <input
            v-model="searchRATING"
            @input="search"
            placeholder="SEARCH RATING"
          />
        </th>
        <th class="table-header-cell">
          <input
            v-model="searchDirector"
            @input="search"
            placeholder="SEARCH Director"
          />
        </th>
        <th class="table-header-cell">
          <input
            v-model="searchCAST"
            @input="search"
            placeholder="SEARCH CAST"
          />
        </th>
        <th class="table-header-cell">
          <div>
            <label for="durationStart">FROM</label>
            <input
              type="number"
              id="durationStart"
              v-model="durationStart"
              @input="search"
            />
          </div>
          <div>
            <label for="durationEnd">TO</label>
            <input
              type="number"
              id="durationEnd"
              v-model="durationEnd"
              @input="search"
            />
          </div>
        </th>
        <th class="table-header-cell">
          <div>
            <label for="releaseYearStart">FROM</label>
            <input
              type="number"
              id="releaseYearStart"
              v-model="releaseYearStart"
              @input="search"
            />
          </div>
          <div>
            <label for="releaseYearEnd">TO</label>
            <input
              type="number"
              id="releaseYearEnd"
              v-model="releaseYearEnd"
              @input="search"
            />
          </div>
        </th>
        <th class="table-header-cell">
          <input
            v-model="searchCATALOG"
            @input="search"
            placeholder="SEARCH CATALOG"
          />
        </th>
        <th class="table-header-cell">
          <div>
            <label for="status">order：</label>
            <select id="status" v-model="status" @change="search">
              <option value="">...</option>
              <option value="true">descending</option>
              <option value="false">ascending</option>
            </select>
          </div>
        </th>
        <th class="table-header-cell">
          <div>
            <label for="scoreCountStart">FROM</label>
            <input
              type="number"
              id="scoreCountStart"
              v-model="scoreCountStart"
              @input="search"
            />
          </div>
          <div>
            <label for="scoreCountEnd">TO</label>
            <input
              type="number"
              id="scoreCountEnd"
              v-model="scoreCountEnd"
              @input="search"
            />
          </div>
        </th>
        <th class="table-header-cell"></th>
        <th class="table-header-cell">
          <div>
            <button @click="submit">Submit</button>
          </div>
        </th>
      </tr>
      <tr>
        <th class="table-header-cell">ID</th>
        <th class="table-header-cell">NAME</th>
        <th class="table-header-cell">COUNTRY</th>
        <th class="table-header-cell">RATING</th>
        <th class="table-header-cell">DIRECTOR</th>
        <th class="table-header-cell">CAST</th>
        <th class="table-header-cell">DURATION/SEASON</th>
        <th class="table-header-cell">RELEASE_YEAR</th>
        <th class="table-header-cell">CATALOG</th>
        <th class="table-header-cell">AVERAGE_SCORE</th>
        <th class="table-header-cell">SCORE_COUNTS</th>
        <th class="table-header-cell">COMMENTS</th>
        <th class="table-header-cell"></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(film, index) in filmsData" :key="index">
        <td>{{ film.showId }}</td>
        <td>{{ film.name }}</td>
        <td>{{ film.country }}</td>
        <td>{{ film.rating }}</td>
        <td>{{ film.director }}</td>
        <td>{{ film.cast.join(", ") }}</td>
        <td>{{ film.duration }}</td>
        <td>{{ film.release_year }}</td>
        <td>{{ film.catalog.join(", ") }}</td>
        <td>{{ /* Display Score Counts */ }}</td>
        <td>{{ /* Display Comments */ }}</td>
        <td>
          <button @click="goToRatingPage(film)">評分</button>
        </td>
        <td>
          <button @click="deleteFilm(film)">刪除</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: "COMMENT&RATING",
  methods: {
    submit() {
      // 在這裡處理 submit 操作，可以根據需要執行相應的邏輯
      console.log("Submit button clicked!");
    },
    goToRatingPage(film) {
      this.$router.push(`/RatingComponent/${film.showId}`);
    },
    deleteFilm(film) {
      // Implement your deletion logic here
      // You can use this.filmsData to access the array of films
      const index = this.filmsData.indexOf(film);
      if (index !== -1) {
        this.filmsData.splice(index, 1);
      }
    },
    navigateToRating(showId) {
      this.$router.push({
        name: "RatingComponent",
        params: { showId: showId },
      });
    },
  },
  data() {
    return {
      filmsData: [
        {
          showId: "101",
          name: "Shadows",
          country: "United Kingdom",
          rating: "PG",
          director: "li an",
          cast: ["Liam Thompson", "Ella Turner", "Sophie Davis"],
          duration: "2 hours 10 minutes",
          release_year: "2023-07-24",
          catalog: ["Mystery", "Thriller"],
        },
        {
          showId: "101",
          name: "Shadows",
          country: "United Kingdom",
          rating: "PG",
          director: "an",
          cast: ["Liam Thompson", "Ella Turner", "Sophie Davis"],
          duration: "2 hours 10 minutes",
          release_year: "2023-07-24",
          catalog: ["Mystery", "Thriller"],
        },
      ],
    };
  },
};
</script>

<style scoped>
.table-header-cell {
  background-color: #a1d573;
  color: #ffffff;
  padding: 10px;
  text-align: center;

  position: relative;
}
tr {
  background-color: #f0fff0;
  color: #272727;
  padding: 10px;
  text-align: center;

  position: relative;
}
input {
  width: 100%;
  padding: 5px;
  box-sizing: border-box;
}
</style>
