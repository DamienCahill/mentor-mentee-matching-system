import { html } from 'htm/preact';
import { useEffect, useState } from 'preact/hooks';

const ProfileCategorySelector = (props) => {
  const [selectedCategories, setSelectedCategories] = useState([]);
  const [availableCategories, setAvailableCategories] = useState([]);
  useEffect(() => {
    console.log('here');
    fetchCategories();
  }, []);

  async function fetchCategories() {
    let allCategories = [];
    let selectedCategories = [];
    let canBeSelected = [];
    const allCategoriesRes = await fetch( `${props.apiUrl}`, {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Accept': 'application/json',
      }
    });
    
    if( allCategoriesRes.ok ) {
      const json = await allCategoriesRes.json();
      allCategories = json;
    }

    if( ! allCategoriesRes.ok ) {
    }
    const mentorCategoriesRes = await fetch( `${props.apiUrl}/${props.mentorId}`, {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Accept': 'application/json',
      }
    });

    if( mentorCategoriesRes.ok ) {
      const json = await mentorCategoriesRes.json();
      setSelectedCategories(json);
      selectedCategories = json;
      console.log(json);
    }

    if( ! mentorCategoriesRes.ok ) {
    }
    canBeSelected = allCategories.filter(item => !selectedCategories.some(otherItem => JSON.stringify(otherItem) === JSON.stringify(item)));
    setAvailableCategories(canBeSelected);

  }
return html`
  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Selected Categories</h5>
      <ul>
        ${selectedCategories.map((categories, index) => (
          html`<li>${categories[1]}</li>`
        ))}
      </ul>
    </div>
  </div>
  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Available Categories</h5>
      <ul>
        ${availableCategories.map((categories, index) => (
          html`<li>${categories[1]}</li>`
        ))}
      </ul>
    </div>
  </div>
`;

};
export { ProfileCategorySelector };