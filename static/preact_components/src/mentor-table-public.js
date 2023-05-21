import { html } from 'htm/preact';
import { useEffect, useState } from 'preact/hooks';

const MentorsTablePublic = (props) => {
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
    console.log(json)
    $(document).ready(function () {
      $('#mentors-table').DataTable({
        data: json,
        columns: [
          { title: 'First Name', data: 2 },
          { title: 'Last Name', data: 3 },
          { title: 'Email', data: 1 },
          { title: '', data: 0, render: (data, type, row) => {
            return `<a href="/mentors/profiles/${data}">View Profile</a>`;
          }},
        ],
      });
    });
  }

  return html`
    <div class="container px-0">
      <table id="mentors-table" class="table table-striped table-bordered" style="width:100%"></table>
    </div>
  `;
};

export { MentorsTablePublic };