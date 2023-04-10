import { render } from 'preact';
import { html } from 'htm/preact';

import { ProfileCategorySelector } from './profile-category-selector';

const profileCategorySelector = document.getElementById('profile-category-selector');
console.log(profileCategorySelector);
if (profileCategorySelector) {
 render(html`
   <${ProfileCategorySelector} apiUrl=${profileCategorySelector.dataset.apiUrl} mentorId=${profileCategorySelector.dataset.mentorId}
   selectedCategoryIds=${profileCategorySelector.dataset.selectedCategoryIds} />
 `, profileCategorySelector);
}