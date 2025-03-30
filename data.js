<script>
  // Get elements from the HTML
  const form = document.getElementById('data-entry-form');
  const entriesList = document.getElementById('entries-list');

  // Event listener for form submission
  form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent page reload

    // Get values from form fields
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const nic = document.getElementById('nic').value;  // Corrected ID for NIC input
    const company = document.getElementById('company').value;  // Corrected ID for Company input
    const card = document.getElementById('card').value;  // Corrected ID for Issue Card input

    // Check if all fields are filled
    if (name && age && nic && company && card) {
      // Create a new list item with the entered data
      const listItem = document.createElement('li');
      listItem.textContent = `Name: ${name}, Age: ${age}, NIC: ${nic}, Company: ${company}, Issue Card No: ${card}`;

      // Append the new list item to the entries list
      entriesList.appendChild(listItem);

      // Clear form fields
      form.reset();
    } else {
      alert('Please fill in all the fields before submitting.');
    }
  });
</script>
