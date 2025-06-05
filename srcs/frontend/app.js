const { createApp } = Vue;

createApp({
    data() {
        return {
            name: 'Your Name',
            headline: 'Brief description or headline.',
            profileImage: 'images/image.webp',
            posts: [
                { title: 'Welcome to my CV', body: 'This layout mimics LinkedIn using Vue.js.' },
                { title: 'Experience', body: 'Share your professional experience and achievements.' }
            ],
            trending: ['Topic 1', 'Topic 2', 'Topic 3']
        };
    }
}).mount('#app');
