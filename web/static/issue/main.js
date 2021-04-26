function openDetailView(issueId){
    window.open(`/post/${issueId}/`,"_self");
};


function insertAirMarshallResponse(
    status, 
    id, 
    issue_id, 
    value, 
    username, 
    dag_id, 
    task_id,
    ) {
    if ( username === null || username === ""){
      alert("You are not logged in. Please Log In before proceeding");
      var element_id = `form_${status}_${id}`;
      $(`#${element_id}`).val($(`#${element_id} option:first`).val());
      return
    }
    if (value === 'other'){
      value = prompt("Please Elaborate");
      if (value === null || value === ""){
        var element_id = `form_${status}_${id}`
        $(`#${element_id}`).val($(`#${element_id} option:first`).val());
        return
      }
    }
    let dagStartDateTime = $(`#span_dag_start_${issue_id}`).text()
    try{
      $.get(`/api/query/log-issue/?status=${status}` +
      `&id=${id}&issue=${issue_id}`+
      `&option=${value}`+
      `&username=${username}`+
      `&dag=${dag_id}`+
      `&task=${task_id}`+
      `&datetime=${dagStartDateTime}`
      , function(data) {
        if (data.message === "success") {
          $(`.row_${issue_id}`).hide();
          if (status === 'ignore'){
            $('#assign_alert').addClass("alert-warning").removeClass("alert-primary");
            $(`#assign_alert_string`).text('Issue Ignored');
          } else {
            $('#assign_alert').addClass("alert-primary").removeClass("alert-warning");
            $(`#assign_alert_string`).text('Issue Claimed');
          };
          $('#assign_alert').addClass("show").show();
          setTimeout(() => {  $('#assign_alert').removeClass("show"); }, 3000);
        }
      });
    }
    catch(err) {
      var element_id = `form_${status}_${id}`;
      $(`#${element_id}`).val($(`#${element_id} option:first`).val());
      alert(
        "Due to network connectivity" +
        "issues the database was not updated." +
        " Please allow the page to fully load before clearing out issues")
      return
    }
};

function openDagId(dag_id, run_id) {
    window.open(
    );
};