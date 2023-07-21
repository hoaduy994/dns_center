$(function () {
  $('#forwarder_table').DataTable();

  $('#forwarder_table').on('click', '.del-forwarder-list', function () {
    let idDnsNode = $(this).data("iddnsnode")

    let idDnsForward = $(this).data("iddnsforward")

    $('.input-id-dnsnode').val(idDnsNode);
    $('.input-id-dnsforward').val(idDnsForward);

  });

  $('#modalDeleteDnsForward').on('hidden.bs.modal', function (e) {
    $('.input-id-dnsnode').val("");
    $('.input-id-dnsforward').val("");
  })

  $('.btn-dns-forward-form').click(function (e) {
    e.preventDefault();

    $('.ip-dns-forward').keyup(function () {
      $('.ip-dns-forward-err').css({ "display": "none" });
    });

    $('.title-dns-forward').keyup(function () {
      $('.title-dns-forward-err').css({ "display": "none" });
    });

    let ipaddress = $('.ip-dns-forward').val();
    let title = $('.title-dns-forward').val();

    if (!ValidateNull(ipaddress)) {
      $('.ip-dns-forward-err').text("IP address is required !");
      $('.ip-dns-forward-err').css({ "display": "block" });
    } else if (!ValidateIPaddress(ipaddress)) {
      $('.ip-dns-forward-err').text("Invalid IP address !");
      $('.ip-dns-forward-err').css({ "display": "block" });
    }

    if (!ValidateNull(title)) {
      $('.title-dns-forward-err').text("Title is required !");
      $('.title-dns-forward-err').css({ "display": "block" });
    }

    if (ValidateNull(ipaddress) && ValidateIPaddress(ipaddress) && ValidateNull(title)) {
      $('.dns-forward-form').submit();
    }
  })

  function ValidateIPaddress(ipaddress) {
    if (/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(ipaddress)) {
      return (true)
    }
    return (false)
  }

  function ValidateNull(data) {
    data = data.trim().length;
    if (data && data > 0) {
      return (true)
    }
    return (false)
  }
});
