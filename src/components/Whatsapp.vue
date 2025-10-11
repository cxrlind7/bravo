<template>
  <!-- Botón flotante -->
  <button class="whatsapp-btn">
    <i class="bi bi-whatsapp"></i>
  </button>
</template>

<script setup>

</script>

<style scoped>
@import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css');

/* Botón flotante */
.whatsapp-btn {
  position: fixed;
  bottom: clamp(12px, 4vw, 20px);
  right: clamp(12px, 4vw, 20px);
  z-index: 1000;
  width: clamp(60px, 16vw, 80px); /* Era 48px-64px, ahora 60px-80px */
  height: clamp(60px, 16vw, 80px); /* Era 48px-64px, ahora 60px-80px */
  border-radius: 50%;
  background-color: #25D366;
  color: white;
  font-size: clamp(28px, 8vw, 36px); /* Era 20px-28px, ahora 28px-36px */
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 16px rgba(37, 211, 102, 0.5);
  animation: breathe 2s ease-in-out infinite;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
}

.whatsapp-btn:hover {
  background-color: #1ebe57;
  transform: scale(1.15);
}


</style>
