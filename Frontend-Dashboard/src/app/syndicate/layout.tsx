import type { Metadata } from "next";
import type { ReactNode } from "react";

export const metadata: Metadata = {
  title: "Syndicate Access",
  description: "Login or sign up to access Syndicate mode."
};

export default function SyndicateAuthLayout({ children }: { children: ReactNode }) {
  return (
    <div className="flex min-h-screen w-full min-w-0 items-center justify-center bg-[#060606] px-4 py-10 text-white pb-[max(2rem,env(safe-area-inset-bottom))] pt-[max(1.5rem,env(safe-area-inset-top))]">
      <div className="w-full max-w-md min-w-0">{children}</div>
    </div>
  );
}
