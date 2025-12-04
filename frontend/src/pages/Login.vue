<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-900 via-gray-900 to-gray-800 p-4">
    <div class="bg-gray-800/50 backdrop-blur-xl border border-gray-700/50 p-8 rounded-2xl shadow-2xl w-full max-w-md">
      <div class="text-center mb-8">
        <!-- <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-purple-600 rounded-2xl flex items-center justify-center text-white font-bold text-2xl mx-auto mb-4 shadow-lg shadow-blue-500/30">
          
        </div> -->
        <h1 class="text-3xl font-bold text-white mb-2">Welcome Back</h1>
        <p class="text-gray-400">Sign in to continue</p>
      </div>
      
      <form @submit.prevent="handleSubmit" class="space-y-5">
        <div>
          <label class="block text-gray-300 text-sm font-semibold mb-2">Username</label>
          <input
            v-model="username"
            type="text"
            class="w-full border border-gray-600/50 bg-gray-900/50 text-white placeholder-gray-500 p-3 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/50 transition-all backdrop-blur-sm"
            placeholder="Enter your username"
            required
          />
        </div>
        
        <div>
          <label class="block text-gray-300 text-sm font-semibold mb-2">Password</label>
          <input
            v-model="password"
            type="password"
            class="w-full border border-gray-600/50 bg-gray-900/50 text-white placeholder-gray-500 p-3 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/50 transition-all backdrop-blur-sm"
            placeholder="Enter your password"
            required
          />
        </div>
        
        <button
          type="submit"
          :disabled="isLoading"
          class="w-full bg-blue-600 hover:bg-blue-500 text-white py-3.5 px-6 rounded-lg font-medium transition-all duration-200 hover:shadow-lg hover:-translate-y-0.5 disabled:opacity-60 disabled:cursor-not-allowed disabled:hover:translate-y-0 disabled:hover:shadow-none flex items-center justify-center gap-2"
        >
          <svg v-if="isLoading" class="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <span>{{ isLoading ? 'Signing in...' : 'Sign In' }}</span>
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const isLoading = ref(false);
const userStore = useUserStore();
const router = useRouter();

const handleSubmit = async () => {
  isLoading.value = true;
  try {
    const success = await userStore.login(username.value, password.value);
    if (success) {
      if (userStore.user.role === "admin") {
        router.push("/admin");
      } else {
        router.push("/");
      }
    } else {
      alert("Login failed");
    }
  } finally {
    isLoading.value = false;
  }
};
</script>
