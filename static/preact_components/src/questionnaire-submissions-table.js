import { html } from 'htm/preact';
import { useEffect, useState } from 'preact/hooks';

const QuestionnaireSubmissionsTable = (props) => {
  useEffect(() => {
    createTable();
  }, []);
  function formatDate(timestamp) {
    const dateObject = new Date(timestamp * 1000);

    // Format the date as DD/MM/YYYY
    const day = dateObject.getDate().toString().padStart(2, '0');
    const month = (dateObject.getMonth() + 1).toString().padStart(2, '0');
    const year = dateObject.getFullYear().toString();
    const formattedDate = `${day}/${month}/${year}`;
    return formattedDate;
  }
  async function createTable() {
    const res = await fetch(
      props.apiUrl,
      {
        method: 'GET',
      }
    );
    const json = await res.json();
    const tabledata = json.data;
    console.log(json);
    $(document).ready(function () {
      $('#questionnaire-submissions-table').DataTable({
        data: json,
        columns: [
          { title: 'Submissions Id', data: 0 },
          { title: 'Submitted By', data: 2 },
          { title: 'Submission Date', data: 1, render: (data, type, row) => {
            return formatDate(data);
          }},
          { title: '', data: 0, render: (data, type, row) => {
            return `<a href="/questionnaires/submission/${data}">View Submission</a>`;
          }}
        ],
      });
    });
  }

  return html`
    <div class="container px-0">
      <table id="questionnaire-submissions-table" class="table table-striped table-bordered" style="width:100%"></table>
    </div>
  `;
};

export { QuestionnaireSubmissionsTable };