<template>
  <button class="whatsapp-btn" @click="openWhatsApp">
    <i class="bi bi-whatsapp"></i>
  </button>
</template>

<script setup>
// Función para abrir WhatsApp
const openWhatsApp = () => {
  // IMPORTANTE: Reemplaza este número con tu número de WhatsApp
  // Formato: código de país + número (sin +, espacios o guiones)
  const phoneNumber = '521234567890'; 
  
  const url = `https://wa.me/${phoneNumber}`;
  
  // Abre el enlace en una nueva pestaña
  window.open(url, '_blank');
};
</script>

<style scoped>
@import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css');

/* Botón flotante */
.whatsapp-btn {
  position: fixed;
  bottom: clamp(12px, 4vw, 20px);
  right: clamp(12px, 4vw, 20px);
  z-index: 1000;
  width: clamp(60px, 16vw, 80px);
  height: clamp(60px, 16vw, 80px);
  border-radius: 50%;
  background-color: #25D366;
  color: white;
  font-size: clamp(28px, 8vw, 36px);
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  
  /* La animación 'breathe' ahora controla la escala y la sombra */
  animation: breathe 2s ease-in-out infinite;
}

.whatsapp-btn:hover {
  background-color: #1ebe57;
  /* Hacemos la escala del hover un poco más grande que la animación */
  transform: scale(1.15); 
  /* Pausamos la animación al hacer hover para que el escalado se sienta controlado */
  animation-play-state: paused;
}

/* --- CAMBIO: Definición de la animación --- */
/* Esta animación crea un efecto de "respiración" o pulso */
@keyframes breathe {
  /* Estado inicial y final (normal) */
  0%, 100% {
    transform: scale(1);
    box-shadow: 0 6px 16px rgba(37, 211, 102, 0.5);
  }
  /* Estado intermedio (expansión máxima del pulso) */
  50% {
    transform: scale(1.05);
    /* Hacemos la sombra más grande y notoria en el pico de la animación */
    box-shadow: 0 10px 25px rgba(37, 211, 102, 0.7);
  }
}
</style>