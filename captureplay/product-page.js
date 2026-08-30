(() => {
  const slots = [...document.querySelectorAll('[data-latest-version]')];
  const setVersion = (value) => slots.forEach((node) => { node.textContent = value ? `v${value}` : '—'; });
  fetch('./version.json', { cache: 'no-store' })
    .then((response) => {
      if (!response.ok) throw new Error(`version.json ${response.status}`);
      return response.json();
    })
    .then((data) => {
      const version = String(data?.version || '').trim();
      if (!/^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$/.test(version)) throw new Error('invalid version');
      document.documentElement.dataset.latestVersion = version;
      setVersion(version);
    })
    .catch(() => setVersion(''));
})();
