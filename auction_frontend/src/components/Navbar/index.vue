<script setup lang="ts">
import { RouterView, RouterLink } from 'vue-router'
console.log(document.cookie)
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

        <button v-if="(isLoggedIn !== null)" class="btn btn-outline-success" type="button"
          v-on:click="logout">Logout</button>
        <a v-else class="btn btn-outline-success" type="button" href="http://localhost:8000/login">Login</a>
      </div>
    </div>
  </nav>
  <router-view />
</template>

<script lang="ts">
export default {
  data() {
    return {
      isLoggedIn: this.getCookie('login')
    }
  },
  methods: {
    async logout(e: { preventDefault: () => void; }) {
      e.preventDefault();
      const csrftoken = this.getCookie("csrftoken");
      const response = await fetch('http://localhost:8000/logout/', {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
      });
      this.isLoggedIn = response.status === 200 ? null : this.isLoggedIn
    },

    getCookie(name: string): string | null {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        console.log(cookies)
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      console.log(cookieValue)
      return cookieValue;
    }
  }
}
</script>