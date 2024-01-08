<template>
  <div class="ranking">
    <h2>Top 10 hits</h2>
    <ul class="ranking-list">
      <li
        v-for="(item, index) in sortedItems"
        :key="item.id"
        class="ranking-item"
      >
        <div class="rank">{{ index + 1 }}</div>
        <div class="name">{{ item.name }}</div>
        <div class="score">Score: {{ item.avg_score }}</div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "RankingComponent",
  props: {
    items: {
      type: Array,
      required: true,
    },
  },
  computed: {
    sortedItems() {
      return this.items
        .slice()
        .sort((a, b) => b.score - a.score) // Sort by descending score
        .slice(0, 10); // Get top 10 items
    },
  },
};
</script>

<style>
.ranking {
  text-align: center;
}

.ranking-list {
  list-style-type: none;
  padding: 10;
  margin: 10;
}

.ranking-item {
  display: flex;
  align-items: center;
  margin-bottom: 30px;
  font-size: 0.9em;
}

.rank {
  font-weight: bold;
  margin-right: 30px;
}

.name {
  flex-grow: 10;
}

.score {
  font-weight: bold;
}
</style>
