$(function () {
  $('#list_user_table').DataTable({
    initComplete: function () {
      var column = this.api().column(2);
      // console.log(column);

      var select = $('<select class="form-select filter-role"><option selected value="">Role</option></select>')
        .appendTo('#selectTriggerFilter')
        .on('change', function () {
          var val = $(this).val();
          //column.search(val ? '^' + $(this).val() + '$' : val, true, false).draw();
          column.search(val).draw()
        });

      var offices = [];
      column.data().toArray().forEach(function (s) {
        s = s.split(',');
        s.forEach(function (d) {
          if (!~offices.indexOf(d)) {
            offices.push(d)
            select.append('<option value="' + d + '">' + d + '</option>');
          }
        })
      })
    }
  });

  $('#list_user_table').on('click', '.del-user', function () {
    let id = $(this).data("id")
    $(".input-del-user").val(id);
  });

  $('#modalDeleteUser').on('hidden.bs.modal', function (e) {
    $(".input-del-user").val("");
  })

  $('#list_user_table').on('click', '.update-user', function () {
    let id = $(this).data("id")
    let email = $(this).data("email")
    var rule = $(this).data("rule")
    let username = $(this).data("username")
    let firstname = $(this).data("firstname")
    let lastname = $(this).data("lastname")

    $(".input-update-user-id").val(id);
    $(".input-update-user-email").val(email);
    $(".input-update-user-username").val(username);
    $(".input-update-user-firstname").val(firstname);
    $(".input-update-user-lastname").val(lastname);
    $("input[name=rule][value=" + rule + "]").attr('checked', 'checked');
  });

  $('#modalUpdateUser').on('hidden.bs.modal', function (e) {
    $(".input-update-user-id").val("");
    $(".input-update-user-email").val("");
    $(".input-update-user-username").val("");
    $(".input-update-user-firstname").val("");
    $(".input-update-user-lastname").val("");
    $("input[name=rule]").removeAttr('checked');
  })
});
