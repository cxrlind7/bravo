<template>
  <nav class="navbar">
    <div class="nav-container">
      <!-- <router-link to="/" class="nav-logo">Bravo</router-link> -->
      <router-link to="/" class="nav-logo">
        <img src="/public/logobravo.png" alt="Bravo & Asociados" class="logo-image" />
      </router-link>
      <div class="nav-menu" ref="menu">
        <!-- Home: scroll suave -->
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

        <!-- Otras páginas: router-link -->
        <template v-else>
          <router-link
            to="/#inicio"
            class="nav-link"
            :class="{ active: isInicioActive }"
          >
            Inicio
          </router-link>
        </template>

        <router-link
          to="/aviso-de-privacidad"
          class="nav-link"
          :class="{ active: isLegalActive }"
        >
          Aviso de Privacidad
        </router-link>

        <!-- Barra deslizante -->
        <span class="nav-underline" :style="underlineStyle"></span>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  props: {
    // pásale true en Home y false en las demás páginas
    isHomePage: { type: Boolean, default: false }
  },
  data() {
    return {
      activeSection: this.isHomePage ? 'inicio' : null,
      underlineStyle: { left: '0px', width: '0px' },
      isProgrammaticScroll: false,
      scrollIdleTimer: null
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
    // calcular la sección activa inicial si entras con hash
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
},
  watch: {
    // Cuando cambie la ruta (no-Home), recoloca la barra
    $route() {
      this.$nextTick(() => this.moveUnderline());
    }
  },
  methods: {
    getNavbarHeight() {
      return this.$el?.offsetHeight ?? 80;
    },
    scrollToSection(sectionId) {

      const element = document.getElementById(sectionId);
      if (!element) return;

      const navbarHeight = this.getNavbarHeight();
      const y = element.getBoundingClientRect().top + window.pageYOffset - navbarHeight;

      // Bloquea cambios de activo mientras hace scroll suave
      this.isProgrammaticScroll = true;

      // Marca activo inmediato para mover la barra
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
      // si no hay coincidencia, no cambies el activo
    },
    moveUnderline() {
      const menu = this.$refs.menu;
      if (!menu) return;

      // Prioriza el orden: legal > about > inicio (o el que tenga .active)
      const activeLink =
        menu.querySelector('.nav-link.active') ||
        menu.querySelector('.nav-link.router-link-exact-active') ||
        menu.querySelector('.nav-link.router-link-active');

      if (activeLink) {
        const { offsetLeft, offsetWidth } = activeLink;
        this.underlineStyle = {
          left: `${offsetLeft}px`,
          width: `${offsetWidth}px`
        };
      } else {
        // Si nada está activo, oculta la barra
        this.underlineStyle = { left: '0px', width: '0px' };
      }
    }
  }
};
</script>

<style scoped>
.nav-logo {
  display: flex;
  align-items: center;
}

.logo-image {
  height: 50px; /* Ajusta según tu diseño */
  width: auto;
  object-fit: contain;
  transition: transform 0.3s ease;
}

.logo-image:hover {
  transform: scale(1.05);
}


.navbar {
  background-color: #333333;
  padding: 1rem 0;
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 1000;
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
  color: #fff;
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none;
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
}

.nav-link:hover { color: #ccc; }

/* Clase de "activo" unificada para scroll y router */
.nav-link.active,
.nav-link.router-link-exact-active {
  color: #AFAFAF;
}

/* Barra animada deslizante */
.nav-underline {
  position: absolute;
  bottom: 0;
  height: 2px;
  background-color: #AFAFAF;
  transition: left 250ms cubic-bezier(.25,.8,.25,1),
              width 250ms cubic-bezier(.25,.8,.25,1);
}
/* Responsive */
@media (max-width: 768px) {
  .logo-image {
    height: 40px;
  }
}
</style>
