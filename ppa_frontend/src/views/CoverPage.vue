<template>
  <div class="cover-page">
    <div class="hero text-center">
      
      <h1 class="mb-2">Welcome to <span class="highlight">Placement Portal</span></h1>
      <p class="subtitle mb-4">
        Connecting students with top companies. Apply to drives,<br>
        track your applications and land your dream job.
      </p>

      <div class="illustration mb-4">
        <svg width="320" height="160" viewBox="0 0 320 160" xmlns="http://www.w3.org/2000/svg">
          <!-- Desk -->
          <rect x="60" y="95" width="200" height="6" rx="3" fill="#B5D4F4"/>
          <rect x="80" y="101" width="6" height="30" rx="3" fill="#B5D4F4"/>
          <rect x="234" y="101" width="6" height="30" rx="3" fill="#B5D4F4"/>
          <!-- Laptop -->
          <rect x="110" y="60" width="100" height="68" rx="6" fill="#185FA5"/>
          <rect x="116" y="66" width="88" height="52" rx="4" fill="#E6F1FB"/>
          <rect x="122" y="74" width="55" height="4" rx="2" fill="#185FA5" opacity="0.4"/>
          <rect x="122" y="83" width="45" height="4" rx="2" fill="#185FA5" opacity="0.4"/>
          <rect x="122" y="92" width="50" height="4" rx="2" fill="#185FA5" opacity="0.4"/>
          <rect x="100" y="126" width="120" height="5" rx="2" fill="#85B7EB"/>
          <!-- Person 1 -->
          <circle cx="88" cy="72" r="16" fill="#FAC775"/>
          <rect x="78" y="60" width="20" height="8" rx="2" fill="#2C2C2A"/>
          <ellipse cx="88" cy="60" rx="18" ry="5" fill="#444441"/>
          <circle cx="84" cy="70" r="2" fill="#2C2C2A"/>
          <circle cx="92" cy="70" r="2" fill="#2C2C2A"/>
          <path d="M84 77 Q88 81 92 77" stroke="#2C2C2A" stroke-width="1.5" fill="none"/>
          <rect x="72" y="86" width="32" height="26" rx="8" fill="#6c5ce7"/>
          <rect x="64" y="95" width="10" height="18" rx="5" fill="#6c5ce7"/>
          <rect x="94" y="95" width="10" height="18" rx="5" fill="#6c5ce7"/>
          <circle cx="68" cy="113" r="6" fill="#FAC775"/>
          <circle cx="102" cy="113" r="6" fill="#FAC775"/>
          <rect x="76" y="110" width="10" height="18" rx="5" fill="#2C2C2A"/>
          <rect x="88" y="110" width="10" height="18" rx="5" fill="#2C2C2A"/>
          <!-- Person 2 -->
          <circle cx="232" cy="72" r="16" fill="#FAC775"/>
          <rect x="222" y="60" width="20" height="8" rx="2" fill="#2C2C2A"/>
          <ellipse cx="232" cy="60" rx="18" ry="5" fill="#444441"/>
          <circle cx="228" cy="70" r="2" fill="#2C2C2A"/>
          <circle cx="236" cy="70" r="2" fill="#2C2C2A"/>
          <path d="M228 77 Q232 81 236 77" stroke="#2C2C2A" stroke-width="1.5" fill="none"/>
          <rect x="216" y="86" width="32" height="26" rx="8" fill="#e74c3c"/>
          <rect x="208" y="95" width="10" height="18" rx="5" fill="#e74c3c"/>
          <rect x="238" y="95" width="10" height="18" rx="5" fill="#e74c3c"/>
          <circle cx="212" cy="113" r="6" fill="#FAC775"/>
          <circle cx="246" cy="113" r="6" fill="#FAC775"/>
          <rect x="220" y="110" width="10" height="18" rx="5" fill="#2C2C2A"/>
          <rect x="232" y="110" width="10" height="18" rx="5" fill="#2C2C2A"/>
          <!-- Floating cards -->
          <rect x="22" y="48" width="48" height="36" rx="8" fill="#E6F1FB" stroke="#85B7EB" stroke-width="1"/>
          <rect x="30" y="57" width="32" height="3" rx="2" fill="#378ADD" opacity="0.6"/>
          <rect x="30" y="65" width="24" height="3" rx="2" fill="#378ADD" opacity="0.4"/>
          <rect x="30" y="73" width="28" height="3" rx="2" fill="#378ADD" opacity="0.4"/>
          <rect x="250" y="30" width="48" height="36" rx="8" fill="#FAECE7" stroke="#F09975" stroke-width="1"/>
          <rect x="258" y="39" width="32" height="3" rx="2" fill="#D85A30" opacity="0.6"/>
          <rect x="258" y="47" width="24" height="3" rx="2" fill="#D85A30" opacity="0.4"/>
          <rect x="258" y="55" width="28" height="3" rx="2" fill="#D85A30" opacity="0.4"/>
          <!-- Dots -->
          <circle cx="18" cy="30" r="5" fill="#FAC775" opacity="0.8"/>
          <circle cx="300" cy="20" r="5" fill="#85B7EB" opacity="0.8"/>
          <circle cx="308" cy="110" r="4" fill="#e74c3c" opacity="0.7"/>
          <circle cx="12" cy="120" r="4" fill="#3B6D11" opacity="0.7"/>
        </svg>
      </div>

      <div class="btn-row mb-5">
        <router-link to="/login" class="btn btn-primary-custom px-5">Login</router-link>
        <router-link to="/register" class="btn btn-outline-custom px-5">Register</router-link>
      </div>

      <div class="stats-row mx-auto mb-4">
        <div class="stat-card">
          <div class="stat-num">500+</div>
          <div class="stat-label">Students</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">50+</div>
          <div class="stat-label">Companies</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">200+</div>
          <div class="stat-label">Drives</div>
        </div>
      </div>

      <div class="features-row mx-auto">
        <div class="feat-card">
          <div class="feat-icon blue-icon">📋</div>
          <div class="feat-title">Browse drives</div>
          <div class="feat-desc">Find eligible placement drives filtered for you</div>
        </div>
        <div class="feat-card">
          <div class="feat-icon green-icon">👤</div>
          <div class="feat-title">Track status</div>
          <div class="feat-desc">Monitor your applications in real time</div>
        </div>
        <div class="feat-card">
          <div class="feat-icon amber-icon">⭐</div>
          <div class="feat-title">Get reminders</div>
          <div class="feat-desc">Never miss a deadline with auto alerts</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default { name: 'CoverPage' };
</script>

<style scoped>
.cover-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #E6F1FB 0%, #EAF3DE 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.hero { max-width: 620px; margin: auto; }

.badge-pill {
  display: inline-block;
  background: #B5D4F4;
  color: #0C447C;
  font-size: 12px;
  padding: 4px 14px;
  border-radius: 20px;
  font-weight: 500;
}

h1 { font-size: 2rem; font-weight: 500; color: #2c3e50; }
.highlight { color: #185FA5; }

.subtitle { font-size: 1rem; color: #7f8c8d; line-height: 1.7; }

.illustration { display: flex; justify-content: center; }

.btn-row { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }

.btn-primary-custom {
  background: #185FA5;
  color: #E6F1FB;
  border: none;
  border-radius: 30px;
  padding: 10px 32px;
  font-size: 14px;
  text-decoration: none;
}

.btn-outline-custom {
  background: transparent;
  color: #185FA5;
  border: 1.5px solid #185FA5;
  border-radius: 30px;
  padding: 10px 32px;
  font-size: 14px;
  text-decoration: none;
}

.stats-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  max-width: 400px;
}

.stat-card {
  background: white;
  border: 0.5px solid #ddd;
  border-radius: 10px;
  padding: 16px;
  text-align: center;
}

.stat-num { font-size: 1.6rem; font-weight: 500; color: #185FA5; }
.stat-label { font-size: 12px; color: #7f8c8d; margin-top: 4px; }

.features-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  max-width: 500px;
}

.feat-card {
  background: white;
  border: 0.5px solid #ddd;
  border-radius: 12px;
  padding: 18px;
  text-align: left;
}

.feat-icon { font-size: 16px; margin-bottom: 10px; width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; }
.blue-icon { background: #E6F1FB; }
.green-icon { background: #EAF3DE; }
.amber-icon { background: #FAEEDA; }

.feat-title { font-size: 13px; font-weight: 500; color: #2c3e50; margin-bottom: 4px; }
.feat-desc { font-size: 12px; color: #7f8c8d; line-height: 1.5; }
</style>