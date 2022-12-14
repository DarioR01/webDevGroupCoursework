<script setup lang="ts">
import { RouterView, RouterLink } from 'vue-router'
import { getCookie } from '../../utility'
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-3">
    <div class="container-fluid">
      <router-link class="navbar-brand" :to="{ name: 'Home' }">Bidder</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link :to="{ name: 'Home' }" class="nav-link" aria-current="home">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'Profile' }" class="nav-link" aria-current="profile">Profile</router-link>
          </li>
        </ul>

        <button v-if="(isLoggedIn !== '')" class="btn btn-outline-success" type="button"
          v-on:click="logout">Logout</button>
        <a v-else class="btn btn-outline-success" type="button" href="http://localhost:8000/api/login">Login</a>
      </div>
    </div>
  </nav>
  <router-view />
</template>

<script lang="ts">
export default {
  data() {
    return {
      isLoggedIn: getCookie('login') as string
    }
  },
  methods: {
    async logout(e: { preventDefault: () => void; }) {
      e.preventDefault();
      const headers = new Headers([['X-CSRFToken', getCookie('csrftoken')]]);
      const response = await fetch('http://localhost:8000/api/logout/', {
        method: 'POST',
        headers,
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
      });
      this.isLoggedIn = response.status === 200 ? "" : this.isLoggedIn
    },
  }
}
</script>