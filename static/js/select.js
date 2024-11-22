const checkboxes = document.querySelectorAll('.todo-checkbox');
  const actionButtons = document.getElementById('action-buttons');
  
  checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
      let anyChecked = false;
  
      checkboxes.forEach(function(cb) {
        if (cb.checked) {
          anyChecked = true;
        }
      });
  
      if (anyChecked) {
        actionButtons.classList.remove('d-none');
      } else {
        actionButtons.classList.add('d-none');
      }
    });
  });