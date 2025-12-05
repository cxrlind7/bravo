const fs = require("fs");
const path =
  "c:\\Users\\CarlosOmarAldabaEstr\\Documents\\proy\\Bravo\\bravo\\src\\views\\HomeView.vue";

try {
  let content = fs.readFileSync(path, "utf8");
  const lines = content.split(/\r?\n/);

  let foundTemplate = false;
  let foundGlobalCss = false;
  let foundMobileCss = false;

  // 1. Insert Template HTML
  // Look for the closing of services-snap-container
  // We know it's indented with 12 spaces for the closing div of the loop/card? No, the container closing is 12 spaces?
  // Let's look for the sequence:
  //             </div>
  //         </div>
  // And insert between them.

  for (let i = 0; i < lines.length - 1; i++) {
    if (lines[i].trim() === "</div>" && lines[i + 1].trim() === "</div>") {
      // Check context: previous line should be closing of service-card or similar
      // line i is closing services-snap-container (12 spaces)
      // line i+1 is closing #services (8 spaces)
      // Let's check indentation roughly
      if (
        lines[i].includes("            </div>") &&
        lines[i + 1].includes("        </div>")
      ) {
        lines.splice(
          i + 1,
          0,
          '            <p class="swipe-indicator">Desliza &rarr;</p>'
        );
        foundTemplate = true;
        break;
      }
    }
  }

  // 2. Insert Global CSS
  // Insert before .services-subtitle
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes(".services-subtitle {")) {
      lines.splice(i, 0, ".swipe-indicator {\n    display: none;\n}\n");
      foundGlobalCss = true;
      break;
    }
  }

  // 3. Insert Mobile CSS
  // Insert before /* ===== SPECIALIZED AREAS - Apiladas full width ===== */
  const mobileCssBlock = `
    .swipe-indicator {
        display: block;
        text-align: center;
        color: #c9a961;
        font-size: 1rem;
        margin-top: 1rem;
        font-weight: 600;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 0.6; transform: translateX(0); }
        50% { opacity: 1; transform: translateX(5px); }
        100% { opacity: 0.6; transform: translateX(0); }
    }
`;
  for (let i = 0; i < lines.length; i++) {
    if (
      lines[i].includes(
        "/* ===== SPECIALIZED AREAS - Apiladas full width ===== */"
      )
    ) {
      lines.splice(i, 0, mobileCssBlock);
      foundMobileCss = true;
      break;
    }
  }

  if (foundTemplate && foundGlobalCss && foundMobileCss) {
    fs.writeFileSync(path, lines.join("\n"), "utf8");
    console.log("Successfully updated HomeView.vue");
  } else {
    console.log("Failed to update all sections:", {
      foundTemplate,
      foundGlobalCss,
      foundMobileCss,
    });
  }
} catch (err) {
  console.error("Error:", err);
}
