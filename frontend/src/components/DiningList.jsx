import DiningHall from "./DiningHall";

export default function DiningList() {
  return (
    <div>
      <ul className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
        <DiningHall path="/dining/lawson" dist={.05} hMeter={5}>Lawson</DiningHall>
        <DiningHall path="/dining/wiley" dist={.05} hMeter={5}>Wiley</DiningHall>
        <DiningHall path="/dining/windsor" dist={.05} hMeter={5}>Windsor</DiningHall>
      </ul>
    </div>
  );
}