<template>
  <router-link :to="{ name: 'Item', params: { id: id } }">
    <div class="card text-center" style="width: 18rem;">
      <img :src="image" class="card-img-top" alt="..." style="max-height: 12rem;">
      <div class="card-body">
        <h2 class="card-title">{{ title }}</h2>
        <p class="card-text">{{ description }}</p>
      </div>
      <div class="card-footer text-muted">
        <span class="card-subtitle mb-2">{{ price }}£</span>
        <span>{{ (new Date(time)).toString() }}</span>
      </div>
    </div>
  </router-link>
</template>

<script lang="ts">
export default {
  props: {
    id: String,
    title: String,
    description: String,
    price: Number,
    time: { type: Number, default: Date.now() },
    image: String,
  }
}
</script>