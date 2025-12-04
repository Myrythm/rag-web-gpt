<template>
  <div
    :class="['flex mb-6', message.role === 'user' ? 'justify-end' : 'justify-start']"
  >
    <div
      :class="[
        'max-w-[80%] p-4 rounded-2xl shadow-lg transition-all duration-200 hover:shadow-xl',
        message.role === 'user'
          ? 'bg-gradient-to-br from-blue-600 to-purple-600 text-white rounded-br-none'
          : 'bg-gray-800/50 backdrop-blur-xl border border-gray-700/50 text-gray-100 rounded-bl-none',
      ]"
    >
      <!-- Loading indicator for assistant -->
      <div v-if="message.role === 'assistant' && message.streaming && !message.content" class="flex items-center gap-2">
        <div class="flex space-x-1">
          <div class="w-2 h-2 bg-blue-400 rounded-full animate-bounce" style="animation-delay: 0ms"></div>
          <div class="w-2 h-2 bg-blue-400 rounded-full animate-bounce" style="animation-delay: 150ms"></div>
          <div class="w-2 h-2 bg-blue-400 rounded-full animate-bounce" style="animation-delay: 300ms"></div>
        </div>
      </div>

      <!-- Render markdown for assistant messages -->
      <div v-else-if="message.role === 'assistant'">
        <MarkdownRenderer :content="message.content" />
        <span 
          v-if="message.streaming && message.content" 
          class="inline-block w-2 h-4 ml-1 bg-blue-400 animate-pulse align-middle"
        ></span>
      </div>

      <!-- Plain text for user messages -->
      <p v-else class="whitespace-pre-wrap leading-relaxed text-[15px]">
        {{ message.content }}
      </p>
    </div>
  </div>
</template>

<script setup>
import MarkdownRenderer from './MarkdownRenderer.vue';

defineProps(["message"]);
</script>

