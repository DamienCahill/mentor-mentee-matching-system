import { render } from 'preact';
import { html } from 'htm/preact';

import { ProfileCategorySelector } from './profile-category-selector';
import { AdminsTable } from './admins-table';
import { MentorsTable } from './mentors-table';
import { QuestionnaireSubmissionsTable } from './questionnaire-submissions-table';
import { ProposedMatchesTable } from './proposed-matches-table.js';
import { MentorMatchesTable } from './mentor-matches-table.js';
import { AcceptedMatchesTable } from './accepted-matches-table.js';
import { MentorsTablePublic } from './mentor-table-public';
import { PublicProfileCategory } from './public-profile-category';

const profileCategorySelector = document.getElementById('profile-category-selector');
const publicProfileCategory = document.getElementById('public-profile-category');
const adminsTable  = document.getElementById('admins-table-element');
const mentorsTable = document.getElementById('mentors-table-element');
const submissionsTable = document.getElementById('submissions-table-element');
const proposedMatchesTable = document.getElementById('proposed-matches-table-element');
const mentorMatchesTable = document.getElementById('mentor-matches-table-element');
const acceptedMatchesTable = document.getElementById('accepted-matches-table-element');
const mentorsTablePublic = document.getElementById('mentors-table-public-element');

if (profileCategorySelector) {
 render(html`
   <${ProfileCategorySelector} apiUrl=${profileCategorySelector.dataset.apiUrl} mentorId=${profileCategorySelector.dataset.mentorId}
   selectedCategoryIds=${profileCategorySelector.dataset.selectedCategoryIds} />
 `, profileCategorySelector);
}

console.log(publicProfileCategory);
if (publicProfileCategory) {
 render(html`
   <${PublicProfileCategory} apiUrl=${publicProfileCategory.dataset.apiUrl} mentorId=${publicProfileCategory.dataset.mentorId}
   selectedCategoryIds=${publicProfileCategory.dataset.selectedCategoryIds} />
 `, publicProfileCategory);
}

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


if (submissionsTable) {
 render(html`
   <${QuestionnaireSubmissionsTable} apiUrl=${submissionsTable.dataset.apiUrl} />
 `, submissionsTable);
}

if (proposedMatchesTable) {
 render(html`
   <${ProposedMatchesTable} apiUrl=${proposedMatchesTable.dataset.apiUrl} mentorId=${proposedMatchesTable.dataset.mentorId}/>
 `, proposedMatchesTable);
}

if (mentorMatchesTable) {
 render(html`
   <${MentorMatchesTable} apiUrl=${mentorMatchesTable.dataset.apiUrl} />
 `, mentorMatchesTable);
}

if (acceptedMatchesTable) {
 render(html`
   <${AcceptedMatchesTable} apiUrl=${acceptedMatchesTable.dataset.apiUrl} />
 `, acceptedMatchesTable);
}
console.log(mentorsTablePublic)
if (mentorsTablePublic) {
 render(html`
   <${MentorsTablePublic} apiUrl=${mentorsTablePublic.dataset.apiUrl} />
 `, mentorsTablePublic);
}