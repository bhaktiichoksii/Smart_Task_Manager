/* ==========================================================================
   SMART TASK MANAGER - JAVASCRIPT INTERACTIONS
   Simple, clean, and beginner-friendly JavaScript functions
   ========================================================================== */

document.addEventListener("DOMContentLoaded", function () {
    // ----------------------------------------------------------------------
    // 1. SIDEBAR TOGGLE FUNCTIONALITY FOR DASHBOARD
    // ----------------------------------------------------------------------
    const menuBtn = document.getElementById("menu-btn");
    const sidebar = document.getElementById("sidebar");
    const backdrop = document.getElementById("sidebar-backdrop");

    if (menuBtn) {
        menuBtn.addEventListener("click", function (e) {
            e.preventDefault();
            if (sidebar) {
                // Toggle collapsed class on desktop and show class on mobile
                sidebar.classList.toggle("collapsed");
                sidebar.classList.toggle("show");
                if (backdrop) {
                    backdrop.classList.toggle("show");
                }
            } else {
                // If clicked on a page without a sidebar, navigate to dashboard
                window.location.href = "/dashboard";
            }
        });
    }

    if (backdrop && sidebar) {
        backdrop.addEventListener("click", function () {
            sidebar.classList.remove("show");
            sidebar.classList.remove("collapsed");
            backdrop.classList.remove("show");
        });
    }

    // ----------------------------------------------------------------------
    // 2. AUTO CLOSE FLASH ALERTS AFTER 5 SECONDS
    // ----------------------------------------------------------------------
    const flashAlerts = document.querySelectorAll(".flash-alert");
    flashAlerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.opacity = "0";
            setTimeout(function () {
                alert.remove();
            }, 300);
        }, 5000);
    });
});

// --------------------------------------------------------------------------
// 3. TOGGLE PASSWORD VISIBILITY (SHOW / HIDE PASSWORD)
// --------------------------------------------------------------------------
function togglePasswordVisibility(inputId, eyeIconId) {
    const passwordInput = document.getElementById(inputId);
    const eyeIcon = document.getElementById(eyeIconId);

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIcon.classList.remove("fa-eye");
        eyeIcon.classList.add("fa-eye-slash");
    } else {
        passwordInput.type = "password";
        eyeIcon.classList.remove("fa-eye-slash");
        eyeIcon.classList.add("fa-eye");
    }
}

// --------------------------------------------------------------------------
// 4. CHECK PASSWORD STRENGTH ON REGISTER PAGE
// --------------------------------------------------------------------------
function checkPasswordStrength(password) {
    const strengthBar = document.getElementById("strength-bar");
    const strengthText = document.getElementById("strength-text");

    if (!strengthBar || !strengthText) return;

    let score = 0;

    if (password.length >= 6) score += 1;
    if (password.length >= 8) score += 1;
    if (/[A-Z]/.test(password)) score += 1;
    if (/[0-9]/.test(password)) score += 1;

    if (password.length === 0) {
        strengthBar.style.width = "0%";
        strengthText.innerText = "Password strength: Empty";
        strengthText.style.color = "#64748b";
    } else if (score <= 1) {
        strengthBar.style.width = "25%";
        strengthBar.style.backgroundColor = "#ef4444"; // Red
        strengthText.innerText = "Password strength: Weak";
        strengthText.style.color = "#ef4444";
    } else if (score === 2 || score === 3) {
        strengthBar.style.width = "65%";
        strengthBar.style.backgroundColor = "#f59e0b"; // Yellow/Orange
        strengthText.innerText = "Password strength: Medium";
        strengthText.style.color = "#f59e0b";
    } else {
        strengthBar.style.width = "100%";
        strengthBar.style.backgroundColor = "#10b981"; // Green
        strengthText.innerText = "Password strength: Strong";
        strengthText.style.color = "#10b981";
    }
}

// --------------------------------------------------------------------------
// 5. VALIDATE REGISTER FORM PASSWORDS MATCH
// --------------------------------------------------------------------------
function validateRegisterForm() {
    const password = document.getElementById("reg-password").value;
    const confirmPassword = document.getElementById("reg-confirm-password").value;
    const matchError = document.getElementById("match-error");

    if (password !== confirmPassword) {
        if (matchError) {
            matchError.innerText = "Passwords do not match! Please check again.";
        } else {
            alert("Passwords do not match!");
        }
        return false; // Prevent form submission
    }

    if (matchError) {
        matchError.innerText = "";
    }
    return true; // Allow submission
}