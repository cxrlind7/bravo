<template>
  <nav class="navbar">
    <div class="nav-container">
      <router-link to="/" class="nav-logo" @click="closeMenu">
        <img src="/public/logobravo.png" alt="Bravo & Asociados" class="logo-image" />
      </router-link>

      <button
        class="nav-toggle"
        @click="toggleMenu"
        :class="{ 'is-open': isMenuOpen }"
        aria-label="Toggle navigation"
        aria-expanded="isMenuOpen"
      >
        <span></span>
        <span></span>
        <span></span>
      </button>

      <div class="nav-menu" :class="{ 'is-open': isMenuOpen }" ref="menu">
        <template v-if="isHomePage">
          <a
            @click="scrollToSection('inicio')"
            class="nav-link"
            :class="{ active: isInicioActive }"
          >
            Inicio
          </a>
          <a
            @click="scrollToSection('about')"
            class="nav-link"
            :class="{ active: isAboutActive }"
          >
            Nosotros
          </a>
          <a
            @click="scrollToSection('services')"
            class="nav-link"
            :class="{ active: isServicesActive }"
          >
            Servicios
          </a>
        </template>

        <template v-else>
          <router-link to="/#inicio" class="nav-link" @click="closeMenu">
            Inicio
          </router-link>
        </template>

        <router-link
          to="/aviso-de-privacidad"
          class="nav-link"
          :class="{ active: isLegalActive }"
          @click="closeMenu"
        >
          Aviso de Privacidad
        </router-link>

        <span class="nav-underline" :style="underlineStyle"></span>
      </div>

      <div v-if="isMenuOpen" class="nav-overlay" @click="closeMenu"></div>
    </div>
  </nav>
</template>

<script>
export default {
  props: {
    isHomePage: { type: Boolean, default: false }
  },
  data() {
    return {
      activeSection: this.isHomePage ? 'inicio' : null,
      underlineStyle: { left: '0px', width: '0px' },
      isProgrammaticScroll: false,
      scrollIdleTimer: null,
      isMenuOpen: false // <-- CAMBIO: Estado para el menú hamburguesa
    };
  },
  computed: {
    isInicioActive() {
      return this.activeSection === 'inicio';
    },
    isAboutActive() {
      return this.activeSection === 'about';
    },
    isServicesActive() {
      return this.activeSection === 'services';
    },
    isLegalActive() {
      return this.$route.path === '/aviso-de-privacidad';
    }
  },
  mounted() {
    window.addEventListener('resize', this.moveUnderline, { passive: true });
    if (this.isHomePage) {
      window.addEventListener('scroll', this.updateActiveSection, { passive: true });
      this.$nextTick(() => {
        this.computeActiveSection();
        this.moveUnderline();
      });
    } else {
      this.$nextTick(() => this.moveUnderline());
    }
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.moveUnderline);
    if (this.isHomePage) {
      window.removeEventListener('scroll', this.updateActiveSection);
    }
    clearTimeout(this.scrollIdleTimer);
    // Limpia el bloqueo de scroll del body si el componente se destruye
    document.body.style.overflow = '';
  },
  watch: {
    $route() {
      this.$nextTick(() => this.moveUnderline());
    },
    // <-- CAMBIO: Observador para bloquear/desbloquear el scroll del body
    isMenuOpen(isOpen) {
      document.body.style.overflow = isOpen ? 'hidden' : '';
      // Recalcular la barra cuando se abre/cierra el menú por si cambia el tamaño de la ventana
      this.$nextTick(() => this.moveUnderline());
    }
  },
  methods: {
    // <-- CAMBIO: Métodos para controlar el menú
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    closeMenu() {
      this.isMenuOpen = false;
    },
    getNavbarHeight() {
      return this.$el?.offsetHeight ?? 80;
    },
    scrollToSection(sectionId) {
      this.closeMenu(); // <-- CAMBIO: Cierra el menú al hacer clic en un enlace

      const element = document.getElementById(sectionId);
      if (!element) return;

      const navbarHeight = this.getNavbarHeight();
      const y = element.getBoundingClientRect().top + window.pageYOffset - navbarHeight;

      this.isProgrammaticScroll = true;
      this.activeSection = sectionId;
      this.$nextTick(() => this.moveUnderline());

      window.scrollTo({ top: y, behavior: 'smooth' });

      clearTimeout(this.scrollIdleTimer);
      this.scrollIdleTimer = setTimeout(() => {
        this.isProgrammaticScroll = false;
        this.computeActiveSection();
        this.$nextTick(() => this.moveUnderline());
      }, 500);
    },
    updateActiveSection() {
      if (this.isProgrammaticScroll) {
        clearTimeout(this.scrollIdleTimer);
        this.scrollIdleTimer = setTimeout(() => {
          this.isProgrammaticScroll = false;
          this.computeActiveSection();
          this.$nextTick(() => this.moveUnderline());
        }, 150);
        return;
      }
      this.computeActiveSection();
      this.$nextTick(() => this.moveUnderline());
    },
    computeActiveSection() {
      const sections = ['inicio', 'about', 'services'];
      const navbarHeight = this.getNavbarHeight();
      const anchorY = navbarHeight + 1;

      for (const id of sections) {
        const el = document.getElementById(id);
        if (!el) continue;
        const rect = el.getBoundingClientRect();
        if (rect.top <= anchorY && rect.bottom > anchorY) {
          this.activeSection = id;
          return;
        }
      }
    },
    moveUnderline() {
      const menu = this.$refs.menu;
      if (!menu) return;

      const activeLink =
        menu.querySelector('.nav-link.active') ||
        menu.querySelector('.nav-link.router-link-exact-active');

      if (activeLink) {
        const { offsetLeft, offsetWidth } = activeLink;
        this.underlineStyle = {
          left: `${offsetLeft}px`,
          width: `${offsetWidth}px`
        };
      } else {
        this.underlineStyle = { left: '0px', width: '0px' };
      }
    }
  }
};
</script>

<style scoped>
/* --- Estilos Base (Escritorio) --- */
.navbar {
  background-color: #333333;
  padding: 1rem 0;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  transition: background-color 0.3s ease;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  font-size: 1.4rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2rem;
}

.nav-logo {
  display: flex;
  align-items: center;
  z-index: 1010; /* Para que esté por encima del overlay */
}

.logo-image {
  height: 50px;
  width: auto;
  object-fit: contain;
  transition: transform 0.3s ease;
}

.logo-image:hover {
  transform: scale(1.05);
}

.nav-menu {
  display: flex;
  gap: 2rem;
  position: relative;
}

.nav-link {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
  padding: 0.5rem 0;
  position: relative;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #ccc;
}

.nav-link.active,
.nav-link.router-link-exact-active {
  color: #AFAFAF;
}

.nav-underline {
  position: absolute;
  bottom: 0;
  height: 2px;
  background-color: #AFAFAF;
  transition: left 250ms cubic-bezier(.25, .8, .25, 1), width 250ms cubic-bezier(.25, .8, .25, 1);
}

/* --- CAMBIO: Elementos de móvil ocultos en escritorio --- */
.nav-toggle {
  display: none;
}
.nav-overlay {
  display: none;
}


/* --- CAMBIO: Estilos Responsivos para Móvil --- */
@media (max-width: 768px) {
  .logo-image {
    height: 40px;
  }

  /* --- Menú Deslizable --- */
  .nav-menu {
    position: fixed;
    top: 0;
    right: -100%; /* Inicia fuera de la pantalla */
    width: 70%;
    max-width: 300px;
    height: 100vh;
    background-color: #222;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 2.5rem;
    transition: right 0.4s cubic-bezier(0.23, 1, 0.32, 1);
    z-index: 1005;
    padding-top: 60px; /* Espacio para el logo y botón de cierre */
  }

  .nav-menu.is-open {
    right: 0; /* Lo trae a la vista */
    box-shadow: -5px 0 15px rgba(0, 0, 0, 0.2);
  }

  .nav-link {
    font-size: 1.5rem;
    color: #f0f0f0;
  }

  /* La barra deslizante no es necesaria en el menú vertical */
  .nav-underline {
    display: none;
  }

  /* --- Botón de Hamburguesa --- */
  .nav-toggle {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    width: 30px;
    height: 24px;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
    z-index: 1010; /* Por encima de todo */
  }

  .nav-toggle span {
    width: 100%;
    height: 3px;
    background-color: #fff;
    border-radius: 2px;
    transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1);
    position: relative;
    transform-origin: center;
  }

  /* Animación a 'X' cuando el menú está abierto */
  .nav-toggle.is-open span:nth-child(1) {
    transform: translateY(10.5px) rotate(45deg);
  }
  .nav-toggle.is-open span:nth-child(2) {
    opacity: 0;
  }
  .nav-toggle.is-open span:nth-child(3) {
    transform: translateY(-10.5px) rotate(-45deg);
  }

  /* --- Overlay --- */
  .nav-overlay {
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1001; /* Detrás del menú pero por encima del contenido */
  }
}
</style>