import { render } from 'preact';
import { html } from 'htm/preact';

import { ProfileCategorySelector } from './profile-category-selector';
import { AdminsTable } from './admins-table';
import { MentorsTable } from './mentors-table';

const profileCategorySelector = document.getElementById('profile-category-selector');
const adminsTable  = document.getElementById('admins-table-element');
const mentorsTable = document.getElementById('mentors-table-element');
console.log(profileCategorySelector);
if (profileCategorySelector) {
 render(html`
   <${ProfileCategorySelector} apiUrl=${profileCategorySelector.dataset.apiUrl} mentorId=${profileCategorySelector.dataset.mentorId}
   selectedCategoryIds=${profileCategorySelector.dataset.selectedCategoryIds} />
 `, profileCategorySelector);
}
console.log(adminsTable)
if (adminsTable) {
 render(html`
   <${AdminsTable} apiUrl=${adminsTable.dataset.apiUrl} />
 `, adminsTable);
}

if (mentorsTable) {
 render(html`
   <${MentorsTable} apiUrl=${mentorsTable.dataset.apiUrl} />
 `, mentorsTable);
}