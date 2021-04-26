function removeResponse(issueId, csrfToken){
    $.post(`/api/post/removeResponse/`,
      {
          issue_id: issueId, 
          csrfmiddlewaretoken: csrfToken
      },
        function( data ) {
          if (data.status === 'success'){
            $('#assign_alert').addClass("show");
            setTimeout(() => {  $('#assign_alert').removeClass("show"); }, 2000);
            $(`.row_${issueId}`).hide();
          }
    });
};

function upsertNote(
    issueId, 
    dagId, 
    taskId,
    user,
    csrfToken){
    let executionTime = $(`#span_dag_start_${issueId}`).text();
    let etlTime = $(`#span_etl_${issueId}`).text();
    $.post(`/api/post/createNoteIfDoesNotExist/`,
    {
        issue_id: issueId,
        dag: dagId,
        task: taskId,
        execution: executionTime,
        etl: etlTime,
        user: user,
        csrfmiddlewaretoken: csrfToken
    },
    function( data ) {
        if (data.status === 'success'){
            window.open(`/post/${issueId}/`,"_self");
        }
    });
};

function hideAssignedRows(){
    let assignedRows = localStorage.getItem('rowAssigned');
    let assignBool = localStorage.getItem('assignBoolean');
    var assignedRowsArray = assignedRows.split(',');
    assignedRowsArray.forEach(function(item, index){
        if (assignBool === 'true'){
            $(`#${item}`).hide();
        } else{
            $(`#${item}`).show();
        }
    });
    if (assignBool === 'true'){
        localStorage.setItem('assignBoolean', 'false');
    } else{
        localStorage.setItem('assignBoolean', 'true');
    }
};

function updateAction(issueId, value){
    if (value === 'other'){
        value = prompt("Please Elaborate");
        if (value === null || value === ""){
            resetAction(issueId);
            return
        }
    }
    $.get(`/api/query/updateAction/?id=${issueId}&action=${value}`, function(data) {
        if (data.status !== 'success'){
            resetAction(issueId);
            return
        }
        $('#assign_alert').addClass("show").addClass("alert-warning").removeClass("alert-primary");
        $('#assign_alert_string').text("Database Updated");
        setTimeout(() => {  $('#assign_alert').removeClass("show").removeClass("alert-warning").addClass("alert-primary"); }, 2000);
    });
};

function resetAction(issueId){
    var elementId = `action_error_${issueId}`;
    $.get(`/api/query/queryAction/?id=${elementId}`, function(data) {
        $(`#${elementId}`).val(data.option);
    });
};

function updateSupportNotes(issueId, htmlId, csrfToken){
    var supportNote = $.trim($(`#${htmlId}`).val());
    $.post(`/api/post/updateSupportNotes/`,
    {
        issue_id: issueId, 
        message: supportNote,
        csrfmiddlewaretoken: csrfToken,
    },
     function( data ) {
        $(`#text_${issueId}`).val(supportNote);
        $('#assign_alert').addClass("show").addClass("alert-warning").removeClass("alert-primary");
        $('#assign_alert_string').text("Database Updated");
        setTimeout(() => {  $('#assign_alert').removeClass("show").removeClass("alert-warning").addClass("alert-primary"); }, 2000);
    });
};

function removeResponse(issueId, csrfToken) {
    $.post(`/api/post/removeResponse/`,
    {
        issue_id: issueId, 
        csrfmiddlewaretoken: csrfToken,
    },
    function(data) {
        if(data.status === 'success'){
            $(`#row_${issueId}`).hide();
            $('#assign_alert').addClass("show").addClass("alert-danger").removeClass("alert-primary");
            $('#assign_alert_string').text("Issue Removed");
            setTimeout(() => {  $('#assign_alert').removeClass("show").removeClass("alert-danger").addClass("alert-primary"); }, 2000);
        }
    });
};

function clearOutAlert(issueId){
    $(`#alert_${issueId}`).removeClass("show");
};

function updateAssignee(
    issueId, 
    assigneeValue, 
    dagId, 
    taskId,
    user,
    csrfToken
    ){
    let executionTime = $(`#span_dag_start_${issueId}`).text();
    let etlTime = $(`#span_etl_${issueId}`).text();
    $.post(`/api/post/updateAssignee/`,
    {
        issue_id: issueId, 
        assignee: assigneeValue,
        dag: dagId,
        execution: executionTime,
        etl: etlTime,
        task: taskId,
        user: user,
        csrfmiddlewaretoken: csrfToken
    },
     function( data ) {
        if (data.status === 'success'){
            $('#assign_alert_string').text("Issue Assigned");
            $('#assign_alert').addClass("show").show();
            $(`#switch_${issueId}`).attr('checked', 'checked');
            setTimeout(() => {  $('#assign_alert').removeClass("show"); }, 2000);
        }
    });
};
