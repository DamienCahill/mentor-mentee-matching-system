import { html } from 'htm/preact';
import { useEffect, useState } from 'preact/hooks';

const MentorMatchesTable = (props) => {
  useEffect(() => {
    createTable();
  }, []);

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
      $('#mentor-matches-table').DataTable({
        data: json,
        columns: [
          { title: 'First Name', data: 2 },
          { title: 'Last Name', data: 3 },
          { title: '', data: 0, render: (data, type, row) => {
            return `<a href="/matches/proposed/${data}">View Proposed Matches</a>`;
          }},
           { title: '', data: 0, render: (data, type, row) => {
            return `<a href="/matches/accepted/${data}">View Accepted Matches</a>`;
          }}
        ],
      });
    });
  }

  return html`
    <div class="container px-0">
      <table id="mentor-matches-table" class="table table-striped table-bordered" style="width:100%"></table>
    </div>
  `;
};

export { MentorMatchesTable };