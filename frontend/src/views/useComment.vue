<template>
  <table>
    <thead>
      <tr>
        <th class="table-header-cell">
          <input v-model="searchID"  placeholder="SEARCH ID" />
        </th>
        <th class="table-header-cell">
          <input
            v-model="searchName"
            
            placeholder="SEARCH NAME"
          />
        </th>
        <th class="table-header-cell">
          <input
            v-model="searchCOUNTRY"
            
            placeholder="SEARCH COUNTRY"
          />
        </th>
        <th class="table-header-cell">
          <input
            v-model="searchRATING"
            
            placeholder="SEARCH RATING"
          />
        </th>
        <th class="table-header-cell">
          <input
            v-model="searchDirector"
            
            placeholder="SEARCH Director"
          />
        </th>
        <th class="table-header-cell">
          <input
            v-model="searchCAST"
            
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
              
            />
          </div>
          <div>
            <label for="durationEnd">TO</label>
            <input
              type="number"
              id="durationEnd"
              v-model="durationEnd"
              
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
              
            />
          </div>
          <div>
            <label for="releaseYearEnd">TO</label>
            <input
              type="number"
              id="releaseYearEnd"
              v-model="releaseYearEnd"
              
            />
          </div>
        </th>
        <th class="table-header-cell">
          <input
            v-model="searchCATALOG"
            
            placeholder="SEARCH CATALOG"
          />
        </th>
        <th class="table-header-cell">
          <div>
            <label for="status">order：</label>
            <select id="status" v-model="status">
              <option value="">...</option>
              <option value="descending">descending</option>
              <option value="ascending">ascending</option>
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
              
            />
          </div>
          <div>
            <label for="scoreCountEnd">TO</label>
            <input
              type="number"
              id="scoreCountEnd"
              v-model="scoreCountEnd"
              
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
        <th class="table-header-cell"></th>
        <th class="table-header-cell"></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="film in filmsData" :key="film.id">
        <td>{{ film.show_id }}</td>
        <td>{{ film.title }}</td>
        <td>{{ film.country }}</td>
        <td>{{ film.rating }}</td>
        <td>{{ film.director }}</td>
        <td>{{ film.cast }}</td>
        <td>{{ film.duration }}</td>
        <td>{{ film.release_year }}</td>
        <td>{{ film.catalog }}</td>
        <td>{{ film.average_score }}</td>
        <td>{{ film.score_count }}</td>
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
import axios from 'axios'
export default {
  name: "COMMENT-RATING",
  methods: {
    getFormList(){
      axios.get('api/AllForm')
        .then(response =>{
        this.filmsData= response.data
        
        // console.log(this.filmsData)
        // console.log(this.filmsData.data.length)
        // console.log(this.filmsData.data[0].show_id)
        
      })
      .catch(error=>{
        console.log(error)
      })
    },
    async submit() {
      // 在這裡處理 submit 操作，可以根據需要執行相應的邏輯
      console.log(this.searchCAST);
      await axios.get('/api/Filter', { params: {  
        title: this.searchName,
        country: this.searchCOUNTRY,
        rating: this.searchRATING,
        director: this.searchDirector,
        cast: this.searchCAST,
        catalog: this.searchCATALOG,
        release_yearStart: this.releaseYearStart,
        release_yearEnd: this.releaseYearEnd,
        score_countStart: this.scoreCountStart,
        score_countEnd: this.scoreCountEnd,
        status: this.status
      }}).then( response=>{
        console.log(response)
        this.filmsData= response.data
      }).catch(error =>{
        console.log(error)
      });
      this.searchID= '',
      this.searchName= '',
      this.searchCOUNTRY= '',
      this.searchRATING= '',
      this.searchDirector= '',
      this.searchCAST= '',
      this.durationStart= 0,
      this.durationEnd= 0,
      this.releaseYearStart= 0,
      this.releaseYearEnd= 0,
      this.searchCATALOG= '',
      this.status= '...',
      this.scoreCountStart= 0,
      this.scoreCountEnd= 0,
      console.log(this.searchName);
    },
    goToRatingPage(film) {
      this.$router.push(`/RatingComponent/${film.show_id}`);
    },
    deleteFilm(film) {
      // Implement your deletion logic here
      // You can use this.filmsData to access the array of films
       axios.delete(`api/OneForm/${film.show_id}`, {
        data: {show_id: film.show_id}
      }). then(response=>{
        console.log(response)
        this.dataLoad=false
      }). catch(error=>{
        console.log(error)
      })
      ;
      location.reload();

    },
    navigateToRating(film) {
      this.$router.push({
        name: "RatingComponent",
        params: { show_id: film.show_id },
      });
    },
  },
  mounted(){
    if (!this.dataLoad) this.getFormList();
    this.dataLoad=true;
  },
  

  data() {
    return {
      filmsData: {films: []},
      searchID: '',
      searchName: '',
      searchCOUNTRY: '',
      searchRATING: '',
      searchDirector: '',
      searchCAST: '',
      durationStart: 0,
      durationEnd: 0,
      releaseYearStart: 0,
      releaseYearEnd: 0,
      searchCATALOG: '',
      status: '...',
      scoreCountStart: 0,
      scoreCountEnd: 0,
      dataLoad: false,
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