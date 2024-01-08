<template>
  <div id="RatingComponent">
    <header>
      <h1>Rating System</h1>
    </header>

    <main>
      <RatingComponent :initialRating="3" @update-rating="handleRatingUpdate" />
      <CommentSection :comments="comments" @comment-submitted="addComment" />
    </main>
  </div>
</template>

<script>
import RatingComponent from "../components/RatingComponent.vue";
import CommentSection from "../components/CommentSection.vue";
export default {
  name: "App",
  components: {
    RatingComponent,
    CommentSection,
  },
  data() {
    return {
      comments: [], // Initial comments data
    };
  },
  methods: {
    handleRatingUpdate(newRating) {
      // Handle the updated rating
      console.log("New Rating:", newRating);
    },
    addComment(newComment) {
      this.comments.push(newComment);
    },
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
  //background-color: #cde193;
  padding: 10px;
  position: fixed;
  bottom: 0;
  width: 100%;
}
</style>
