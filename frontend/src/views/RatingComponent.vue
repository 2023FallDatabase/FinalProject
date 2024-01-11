<template>
  <div id="RatingComponent">
    <header>
      <h1>Rating System</h1>
    </header>

    <main>
      <RatingComponent :initialRating="3" @update-rating="handleRatingUpdate" :show_id="show_id"/>
      <CommentSection :comments.sync="comments" @submit-comment.prevent :show_id="show_id" />
    </main>
  </div>
</template>

<script>
import RatingComponent from "../components/RatingComponent.vue";
import CommentSection from "../components/CommentSection.vue";
import axios from 'axios'
export default {
  name: "App",
  components: {
    RatingComponent,
    CommentSection,
  },
  data() {
    return {
      id: 0,
      show_id: "",
      comments: [], // Initial comments data
    };
  },
  methods: {
    handleRatingUpdate(newRating) {
      // Handle the updated rating
      console.log("New Rating:", newRating);
      console.log(this.$route.params);
    },
    /*addComment(/*newComment) {
      // this.comments.push(newComment);
      // console.log(this.$route.params.show_id);
      //console.log(newComment);
      
    },*/
    getCommentList(){
      axios.get(`/api/AllComment/${this.show_id}`)
      .then(response=>{
        console.log(response)
        for (let i=0;i<response.data.length;i++){
          const newcomment = {
            id: Date.now(), // 假定每個評論都有一個唯一的ID
            text: response.data[i].comment,
          };
          this.comments.push(newcomment);
          console.log(newcomment);
        }
      }).catch(error=>{
        console.log(error)
      })

    }
  },
  mounted(){
    this.show_id=this.$route.params.show_id;
    this.id=this.$route.params.id;
    this.getCommentList();
  },

};
</script>

<style>
#RatingComponent {
  text-align: center;
  margin-top: 60px;
}

header {
  background-color: #a1d573;
  padding: 15px;
  font-size: 15px;
}

footer {
  background-color: #cde193;
  padding: 10px;
  position: fixed;
  bottom: 0;
  width: 100%;
}
</style>
