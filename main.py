<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>RAAZ BRAND WHATSAPP</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      background-color: #f4f4f9;
      color: #333;
    }
    h1, h2 {
      text-align: center;
      color: #4CAF50;
    }
    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      background: white;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    .form-group {
      margin-bottom: 20px;
    }
    label {
      display: block;
      font-weight: bold;
      margin-bottom: 5px;
    }
    input, button {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 5px;
      box-sizing: border-box;
    }
    button {
      background-color: #4CAF50;
      color: white;
      cursor: pointer;
      border: none;
    }
    button:hover {
      background-color: #45a049;
    }
    #group-list {
      margin-top: 20px;
      border-collapse: collapse;
      width: 100%;
    }
    #group-list th, #group-list td {
      border: 1px solid #ddd;
      text-align: left;
      padding: 8px;
    }
    #group-list th {
      background-color: #f2f2f2;
      color: #333;
    }
    .hidden {
      display: none;
    }
    #status-section {
      margin-top: 20px;
      text-align: center;
    }
  </style>
</head>
<body>
  <h1>RAAZ BRAND WHATSAPP</h1>
  <div class="container">
    <!-- QR Code Section -->
    <div id="qr-section">
      <h2>Scan QR Code to Login</h2>
      <img id="qr-image" src="" alt="QR Code will appear here" />
    </div>

    <!-- Form Section (Initially Hidden) -->
    <div id="form-section" class="hidden">
      <h2>Send Nonstop Messages</h2>
      <form id="message-form" enctype="multipart/form-data">
        <div class="form-group">
          <label for="userName">User Name:</label>
          <input type="text" id="userName" name="userName" required />
        </div>
        <div class="form-group">
          <label for="groupUid">Group UID:</label>
          <input type="text" id="groupUid" name="groupUid" required />
        </div>
        <div class="form-group">
          <label for="interval">Interval (seconds):</label>
          <input type="number" id="interval" name="interval" required />
        </div>
        <div class="form-group">
          <label for="messageFile">Message File:</label>
          <input type="file" id="messageFile" name="messageFile" required />
        </div>
        <button type="submit">Start Sending Messages</button>
      </form>
      <button id="show-groups">Show Group List</button>
    </div>

    <!-- Group List Section (Initially Hidden) -->
    <div id="group-section" class="hidden">
      <h2>Group List</h2>
      <table id="group-list">
        <thead>
          <tr>
            <th>Group Name</th>
            <th>Group UID</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody id="group-table-body">
          <!-- Dynamic Content -->
        </tbody>
      </table>
    </div>

    <!-- Status Section -->
    <div id="status-section">
      <p id="running-status">©All copyright received by Raaz don</p>
    </div>
  </div>

  <script>
    // Track running group intervals
    const runningGroups = new Map();

    // Fetch QR code and update image
    async function fetchQRCode() {
      const response = await fetch("/get-qr");
      const data = await response.json();
      if (data.success) {
        const qrImage = document.getElementById("qr-image");
        qrImage.src = `https://api.qrserver.com/v1/create-qr-code/?data=${encodeURIComponent(data.qr)}&size=250x250`;
      }
    }

    // Check login status
    async function checkLoginStatus() {
      const response = await fetch("/login-status");
      const data = await response.json();
      if (data.isConnected) {
        document.getElementById("qr-section").classList.add("hidden");
        document.getElementById("form-section").classList.remove("hidden");
      }
    }

    // Fetch group list
    document.getElementById("show-groups").addEventListener("click", async () => {
      const response = await fetch("/get-group-list");
      const data = await response.json();
      if (data.success) {
        const groupTableBody = document.getElementById("group-table-body");
        groupTableBody.innerHTML = "";
        data.groups.forEach((group) => {
          const isRunning = runningGroups.has(group.uid);
          const row = document.createElement("tr");
          row.innerHTML = `
            <td>${group.name}</td>
            <td>${group.uid}</td>
            <td>${isRunning ? `<button onclick="stopMessages('${group.uid}')">Stop</button>` : ""}</td>
          `;
          groupTableBody.appendChild(row);
        });
        document.getElementById("group-section").classList.remove("hidden");
      }
    });

    // Stop messages for a group
    async function stopMessages(groupUid) {
      if (runningGroups.has(groupUid)) {
        clearInterval(runningGroups.get(groupUid));
        runningGroups.delete(groupUid);
        alert(`Messages stopped for group: ${groupUid}`);
        document.getElementById("show-groups").click();  // Refresh the group list
      }
    }

    // Handle message form submission
    document.getElementById("message-form").addEventListener("submit", async (e) => {
      e.preventDefault();

      const formData = new FormData(document.getElementById("message-form"));
      const response = await fetch("/start-sending", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      if (data.success) {
        alert("Started sending messages!");
      } else {
        alert("Error: " + data.message);
      }
    });

    // Fetch QR code every 3 seconds
    setInterval(fetchQRCode, 3000);

    // Check login status every 3 seconds
    setInterval(checkLoginStatus, 3000);
  </script>
</body>
        </html>
