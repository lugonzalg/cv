<template>
  <div class="container">
    <header class="header">
      <h1 class="logo">My LinkedIn</h1>
    </header>
    <div class="layout">
      <aside class="sidebar-left">
        <img class="profile" :src="profileImage" alt="Profile" />
        <h2>{{ name }}</h2>
        <p>{{ headline }}</p>
      </aside>
      <main class="feed">
        <article v-for="post in posts" :key="post.title" class="post">
          <h3>{{ post.title }}</h3>
          <p>{{ post.body }}</p>
        </article>
      </main>
      <aside class="sidebar-right">
        <h3>Trending</h3>
        <ul>
          <li v-for="topic in trending" :key="topic">{{ topic }}</li>
        </ul>
      </aside>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const name = ref('Your Name');
const headline = ref('Brief description or headline.');
const profileImage = ref('https://placehold.co/100x100');
const posts = ref([
  { title: 'Welcome', body: 'This layout mimics LinkedIn using Vue.' },
  { title: 'Experience', body: 'Share your professional experience.' }
]);
const trending = ref(['Topic 1', 'Topic 2', 'Topic 3']);
</script>

<style scoped>
.container {
  font-family: Arial, sans-serif;
  background-color: #f3f2ef;
}
.header {
  background-color: #283e4a;
  color: white;
  padding: 1rem;
}
.logo {
  margin: 0;
}
.layout {
  display: flex;
  margin: 1rem;
}
.sidebar-left,
.sidebar-right {
  width: 25%;
  background-color: white;
  padding: 1rem;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.1);
}
.sidebar-left {
  margin-right: 1rem;
}
.sidebar-right {
  margin-left: 1rem;
}
.feed {
  flex: 1;
  background-color: white;
  padding: 1rem;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.1);
}
.post {
  margin-bottom: 1rem;
  border-bottom: 1px solid #ddd;
  padding-bottom: 0.5rem;
}
.profile {
  width: 100%;
  border-radius: 50%;
  margin-bottom: 0.5rem;
}
</style>
